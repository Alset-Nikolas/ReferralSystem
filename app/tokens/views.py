from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View

from .forms import TokenFormActivate
from .models import Token, TokenActivated


class ActivateToken(LoginRequiredMixin, View):
    form_class = TokenFormActivate

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            if Token.objects.filter(id=form.cleaned_data.get('token')).exists():
                token = Token.objects.get(id=form.cleaned_data.get('token'))
                if token.user == self.request.user:
                    request.session['form_err'] = 'Ошибка токена! Свой токен нельзя использовать'
                elif TokenActivated.objects.filter(user=user).exists:
                    request.session['form_err'] = 'Ошибка токена! У пользователя токен уже активирован'
                else:
                    token.users.create(user=user)
                return redirect('users:profile')
        request.session['form_err'] = 'Ошибка токена! Такого нет!'
        return redirect('users:profile')
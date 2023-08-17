from typing import Any, Dict
from django import http
from django.shortcuts import render
from django.views import View
from .backends import PhoneUsernameAuthenticationBackend as PhoneAuth
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import UserFormAuthByTel, UserFormCheckPhone
from django.urls import resolve
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class AuthUserByTelPage(View):

    template_name = "users/auth.html"
    template_name_check_token = 'users/check_token.html'
    form_class = UserFormCheckPhone

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:profile')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = UserFormAuthByTel(request.GET)
        if not form.is_valid() or not request.GET.get('phone'):
            return render(request, self.template_name)
        return render(request, self.template_name_check_token, context={"phone": request.GET.get('phone')})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = PhoneAuth.authenticate(request, phone_number=cd['phone'], phone_token=cd['phone_token'])
            if user:
                login(request, user)
                return redirect('users:profile')
        return render(request, self.template_name_check_token, {'form': form, 'phone': request.POST.get('phone')})
    
class ProfileUserPage(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)

        if 'form_err' in self.request.session:
            context['form_err'] = self.request.session.pop('form_err')
        if self.request.user.is_authenticated and hasattr(self.request.user, 'token_activated'):
            context['token_activated'] = self.request.user.token_activated
        user = self.request.user
        context['users'] = user.token.users.all()
        return context


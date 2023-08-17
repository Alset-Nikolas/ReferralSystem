from typing import Any, Dict
from django.shortcuts import render
from django.views import View
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import resolve
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TokenFormActivate
from django.urls import reverse
from django.contrib.messages import constants as messages
from .models import TokenActivated, Token

class ActivateToken(LoginRequiredMixin, View):
    form_class = TokenFormActivate

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            if Token.objects.filter(id=form.cleaned_data.get('token')).exists():
                token = Token.objects.get(id=form.cleaned_data.get('token'))
                token.users.create(user=user)
                return redirect('users:profile')
        request.session['form_err'] = 'Ошибка токена! Либо такого нет либо это ваш токен!'
        return redirect('users:profile')
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError
from django.forms import CharField, Form, PasswordInput

from .validators import check_user_phone_token, phone_validator


class UserFormAuthByTel(Form):
    phone = CharField(validators=[phone_validator])

class UserFormCheckPhone(Form):
    phone = CharField(validators=[phone_validator])
    phone_token = CharField(required=True)

    def clean(self) -> bool:
        cleaned_data = super().clean()
        if not check_user_phone_token(cleaned_data.get('phone_token'), cleaned_data.get('phone')):
            raise ValidationError(
                    "Token auth not valid"
                )
        

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
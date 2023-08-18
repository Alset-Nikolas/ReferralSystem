from typing import Any, Dict
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
        

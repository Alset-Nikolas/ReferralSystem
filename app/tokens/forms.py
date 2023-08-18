from uuid import UUID

from django.core.exceptions import ValidationError
from django.forms import CharField, Form, PasswordInput


def validate_token(token):
    return len(token)==6
    
class TokenFormActivate(Form):
    token = CharField(validators=[validate_token])

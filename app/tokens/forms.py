from django.forms import Form, CharField, PasswordInput
from django.core.exceptions import ValidationError
from uuid import UUID

def validate_token(token):
    return len(token)==6
    
class TokenFormActivate(Form):
    token = CharField(validators=[validate_token])

from django.forms import CharField, Form


def validate_token(token):
    return len(token)==6
    
class TokenFormActivate(Form):
    token = CharField(validators=[validate_token])

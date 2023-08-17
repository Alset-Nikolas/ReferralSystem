from django.forms import Form, CharField, PasswordInput
from .validators import phone_validator, check_user_phone_token
from django.core.exceptions import ValidationError

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
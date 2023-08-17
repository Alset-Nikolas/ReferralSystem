from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.db.models import Q
from .validators import check_user_phone_token
from tokens.models import Token

User = get_user_model()



class PhoneUsernameAuthenticationBackend(object):
    @staticmethod
    def authenticate(request, phone_number=None, phone_token=None):
        user=None
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            if check_user_phone_token(phone_token, phone_number):
                user = User.objects.create_user(phone_number=phone_number) 
                Token.objects.create(user=user)
                return user

        if user and check_user_phone_token(phone_token, phone_number):
            return user

        return None

    @staticmethod
    def get_user(user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
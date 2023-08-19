from django.contrib.auth import get_user_model

from .validators import check_user_phone_token

User = get_user_model()



class PhoneUsernameAuthenticationBackend(object):
    @staticmethod
    def authenticate(request, phone_number=None, phone_token=None):
        print('request>>>>>>>>>>>>>>>>>', request)
        user=None
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            if check_user_phone_token(phone_token, phone_number):
                return User.objects.create_user(phone_number=phone_number) 
            
        if user and check_user_phone_token(phone_token, phone_number):
            return user

        return None

    @staticmethod
    def get_user(user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
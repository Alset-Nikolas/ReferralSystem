from django.core.validators import RegexValidator
import typing as t

phone_validator = RegexValidator("^7-([0-9]){3}-([0-9]){3}-([0-9]){4}$", "The phone number provided is invalid")


def check_user_phone_token(phone_token:str,  user_phone:str) -> bool:
    return user_phone and phone_token == user_phone[-4:]
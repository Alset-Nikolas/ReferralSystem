from django.core.validators import RegexValidator

phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")

def check_user_phone_token(phone_token:str, user_phone:str) -> bool:
    return phone_token == user_phone[-4:]
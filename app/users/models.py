from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

from .validators import phone_validator


class UserTelManager(BaseUserManager):
    """
    Custom user model manager where phone is the unique identifiers
    for authentication instead of usernames.
    """
    def __get_password(self, phone_number):
        return phone_number[-4:]

    def create_user(self, phone_number, **extra_fields):
        """
        Create and save a user with the given phone_number.
        """
        if not phone_number:
            raise ValueError(_("The Phone must be set"))
        password = self.__get_password(phone_number)
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, **extra_fields):
        """
        Create and save a SuperUser with the given phone_number.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_admin", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
    
        return self.create_user(phone_number, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=16, validators=[phone_validator], unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone_number'
    objects =  UserTelManager()

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
    

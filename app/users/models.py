from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .validators import phone_validator
from django.contrib.auth.models import AbstractBaseUser, UserManager

class UserTelManager(BaseUserManager):
    """
    Custom user model manager where phone is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, phone_number, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not phone_number:
            raise ValueError(_("The Phone must be set"))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.save()
        return user

    def create_superuser(self, phone, **extra_fields):
        """
        Create and save a SuperUser with the given phone.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=16, validators=[phone_validator], unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone_number'
    objects =  UserTelManager()

    def __str__(self):
        return self.phone_number

    @staticmethod
    def has_perm(perm, obj=None, **kwargs):
        return True

    @staticmethod
    def has_module_perms(app_label, **kwargs):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    

from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string

User = get_user_model()

def get_random_token6():
    return get_random_string(length=6)

class Token(models.Model):
    id = models.CharField(
         primary_key = True,
         default = get_random_token6,
         unique=True,
         max_length=6)
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="token",
        verbose_name="владелец",
    )
    
    def __str__(self):
        return str(self.id) 
    
    @receiver(post_save, sender=User) 
    def create_user_token(sender, instance, created, **kwargs):
        if created:
            Token.objects.create(user=instance)
    
class TokenActivated(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="token_activated",
        unique=True
    )
    token = models.ForeignKey(
        Token,
        on_delete=models.SET_NULL,
        related_name="users",
        verbose_name="владелец",
        null=True
    )
    date = models.DateTimeField(default=datetime.now, blank=True)

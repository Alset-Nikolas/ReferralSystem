from django.contrib import admin

from .models import Token, TokenActivated


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    pass

@admin.register(TokenActivated)
class TokenActivatedAdmin(admin.ModelAdmin):
    pass
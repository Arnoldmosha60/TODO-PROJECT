from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ["username", "email", "contact"]

admin.site.register(CustomUser)

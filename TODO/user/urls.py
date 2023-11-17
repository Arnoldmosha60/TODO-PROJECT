from django.urls import path
from user import views

urlpatterns = [
    path('profile/', views.get_profile),
]
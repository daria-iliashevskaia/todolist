from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from core import views

urlpatterns = [
    path("signup", views.SignupView.as_view()),
    path("login", views.LoginView.as_view()),
    path("profile", views.ProfileView.as_view()),
    path("update_password", views.UpdatePasswordView.as_view()),
]
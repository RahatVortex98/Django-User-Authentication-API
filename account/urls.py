from django.urls import path
from .views import UserRegistrationView,LoginView,ProfileView,ChangePasswordView,ResetPasswordView,ConfirmPasswordView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name="register"),
    path('login/',LoginView.as_view(),name="login"),
    path('dashboard/',ProfileView.as_view(),name="dashboard"),
    path('password-changed/',ChangePasswordView.as_view(),name="change-password"),
    path('password-reset/',ResetPasswordView.as_view(),name="password-reset"),
    path('reset-password-confirm/<uid>/<token>/',ConfirmPasswordView.as_view(),name="reset-password-confirm"),
]

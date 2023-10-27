from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('verify/', VerifyOTPView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('resend-otp/', ResendOTPView.as_view()),
]
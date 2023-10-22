from django.core.mail import send_mail
from django.conf import settings
from .models import User
import random


def send_otp_via_email(email):
    subject = "Your account verification email"
    otp = str(random.randint(100, 999)) + " " + str(random.randint(100, 999))
    message = f'Your otp is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()
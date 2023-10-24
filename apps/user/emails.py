from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from .models import User
import random

def send_otp_via_email(email):
    subject = "Your account verification email"
    otp = random.randint(100_000, 999_999)
    html_message = render_to_string('user/email_verification.html', {'otp': otp})
    from_email = settings.EMAIL_HOST

    message = EmailMessage(subject, html_message, from_email, [email])
    message.content_subtype = 'html'
    message.send()

    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()
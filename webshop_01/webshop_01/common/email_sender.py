import os

from django.contrib import auth
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from webshop_01.users.utils import token_generator

user = auth.get_user_model()


def send_email_message(email, user_id):

    uidb64 = urlsafe_base64_encode(force_bytes(user_id))
    token = token_generator.make_token(user.object.get(id=user_id))

    domain = 'http://127.0.0.1:8000'
    link = reverse('activate', kwargs={
        'uidb64': uidb64,
        'token': token,
    })
    activate_url = 'http://127.0.0.1:8000' + link
    body = f'Thank you for your registration!\nYou are welcome!!\nActivate your account from here {activate_url}'
    sender = os.environ.get('GMAIL_USER')
    header = 'Your Activation Link!'

    email = EmailMessage(
        header,
        body,
        sender,
        [email],
    )

    email.send(fail_silently=False)

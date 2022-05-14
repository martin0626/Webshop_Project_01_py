from django.contrib import auth
from django.db.models.signals import post_save
from django.dispatch import receiver

from webshop_01.common.email_sender import send_email_message
from webshop_01.users.models import Profile
user = auth.get_user_model()


@receiver(post_save, sender=user)
def profile_creator(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
        send_email_message(instance.email, instance.id)

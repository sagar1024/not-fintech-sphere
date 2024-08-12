from django.db.models.signals import post_save
<<<<<<< HEAD
from django.dispatch import receiver
from django.contrib.auth.models import User
=======
from django.contrib.auth.models import User
from django.dispatch import receiver
>>>>>>> 7aacba6 (Implemented users feature)
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
<<<<<<< HEAD
=======

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
>>>>>>> 7aacba6 (Implemented users feature)
        
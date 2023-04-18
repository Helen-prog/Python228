from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def profile_update(sender, instance, created, **kwargs):
    print("Profile signal")
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )


@receiver(post_save, sender=Profile)
def update_user(sender,  instance, created, **kwargs):
    profile = instance
    user = profile.user
    user.first_name = profile.name
    user.username = profile.username
    user.email = profile.email
    user.save()


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


# post_save.connect(profile_update, sender=Profile)
# post_delete.connect(delete_user, sender=Profile)

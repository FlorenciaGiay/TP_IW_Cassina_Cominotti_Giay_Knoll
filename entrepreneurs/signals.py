from django.dispatch import receiver

# from .models import Entrepreneur, EntrepreneurProfile
# from django.db.models.signals import post_save

# @receiver(post_save, sender=Entrepreneur)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.role == "ENTREPRENEUR":
#         EntrepreneurProfile.objects.create(user=instance)

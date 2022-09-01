from django.dispatch import receiver

# from .models import User, Client, ClientProfile
# from django.db.models.signals import post_save, pre_save

# @receiver(pre_save, sender=User)
# def create_user_admin(sender, instance, **kwargs):
#     if instance.is_superuser and instance.role != "ADMIN":
#         instance.role = "ADMIN"

# @receiver(post_save, sender=Client)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.role == "CLIENT":
#         ClientProfile.objects.create(user=instance)

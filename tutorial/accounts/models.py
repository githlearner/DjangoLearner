from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    city = models.CharField(max_length=50)
    description = models. CharField(max_length=50,default='')
    Phone = models.IntegerField(max_length=10,default=0)

    def __str__(self):
       return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomProfileModel.objects.create(user=instance)
    instance.profile.save()





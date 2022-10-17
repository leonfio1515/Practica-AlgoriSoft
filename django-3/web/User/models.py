from io import open_code
from turtle import onclick
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to = 'users/%Y/%m/%d', null=True, blank=True)

    def get_image(self):
        if self.image:
            return "{}{}".format(settings.MEDIA_URL, self.image)
        return "{}{}".format(settings.STATIC_URL, "img/empty.png")


class BaseModel(models.Model):
    user_creation = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_creation', null=True, blank=True)
    date_creation = models.DateField(auto_now_add=True, null=True, blank=True)
    user_updated = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_updated', null=True, blank=True)
    date_updated = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
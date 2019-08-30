from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class TimestampedModel(models.Model):
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Building(TimestampedModel):

    group_admin = models.ForeignKey(User,on_delete=models.CASCADE)

    name = models.CharField(unique=True,max_length=250)

    price = models.IntegerField(default=0)

    image=models.ImageField(upload_to=settings.BUILDING)

    def __str__(self):
        return  f"{self.name} created"
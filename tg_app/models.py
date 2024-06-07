from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class user_model(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=255)
    picture_url = models.CharField(max_length=255)

class message_model(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=255, blank=False, null=False)
    message_date = models.DateTimeField(timezone.now)
    sender = models.CharField(max_length=255)
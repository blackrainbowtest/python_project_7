from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from datetime import datetime

from .utils import create_shortcode


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Categories(models.Model):
    name = models.CharField(max_length=50)


class Creater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255, default='', blank=True, null=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(Creater, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class FailedLogins(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(default=datetime.now().replace(tzinfo=None), blank=True)
    count = models.IntegerField(default=1)


class PasswordRecovery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(default=datetime.now().replace(tzinfo=None))  # when model is saved
    time_stamp = models.DateTimeField(default=datetime.now().replace(tzinfo=None))  # when model was created

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(PasswordRecovery, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.shortcode = create_shortcode(self)
        super(PasswordRecovery, self).update(*args, **kwargs)

    # def __str__(self):
    #     return str(self.url)
    #
    # def __unicode__(self):
    #     return str(self.url)


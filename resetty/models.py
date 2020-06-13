from django.conf import settings
from django.db import models
from django.db.models.fields import DateField


class ResetPasswordExtra(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    password_last_updated_at = DateField()

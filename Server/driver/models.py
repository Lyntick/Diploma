from django.db import models
from django.contrib.auth.models import User
from route.models import Route

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.TextField()
    name = models.TextField()
    numberRoute = models.OneToOneField(Route, on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.user
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
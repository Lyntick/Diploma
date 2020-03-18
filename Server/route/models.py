from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Stop(models.Model):
    id = models.AutoField(primary_key=True)
    stopName = models.CharField(max_length=80)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Route(models.Model):
    id = models.AutoField(primary_key=True)
    routeName = models.CharField(max_length=100)
    busNumber = models.IntegerField()
    RouteStops = ArrayField(

    )
from django.db import models

# Create your models here.

class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    login = models.CharField(max_length=13)
    password = models.CharField(max_length=30)#помнеять на шифрованую
    busNumber = models.IntegerField()
    govNumber = models.CharField(max_length=50)



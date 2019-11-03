from django.db import models

class User(models.Model):
    user = models.CharField(max_length=50)
    mpg = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)
    destination = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    departure_time = models.DateTimeField()

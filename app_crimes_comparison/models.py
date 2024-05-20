from django.db import models

class User(models.Model):
    id = models.IntegerField()
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

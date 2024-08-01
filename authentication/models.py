from django.db import models

class UsersModel(models.Model):
    name = models.CharField(max_length=200, blank=True)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
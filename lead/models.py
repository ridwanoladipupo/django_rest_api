from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

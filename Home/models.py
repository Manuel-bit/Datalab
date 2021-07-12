from django.db import models

# Create your models here.
class ClientEmail(models.Model):
    email = models.CharField(max_length=20)

class Message(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    email = models.CharField(max_length=20)

    
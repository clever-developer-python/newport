from django.db import models

# Create your models here.

class mails(models.Model):
    text = models.CharField(max_length=100000000)
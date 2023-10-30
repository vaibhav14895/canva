from django.db import models

class Data(models.Model):
    dsa=models.IntegerField(default="0")
    project=models.IntegerField(default="0")
    date=models.DateField(unique=True)
from django.db import models


# Create your models here.
class Animals(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()


class Dogs(models.Model):
    name = models.CharField(max_length=32)
    fk = models.ForeignKey(Animals, null=True, on_delete=models.SET_NULL)

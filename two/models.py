from django.db import models


# Create your models here.
class Animals(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()


class Dogs(models.Model):
    name = models.CharField(max_length=32)
    fk = models.ForeignKey(Animals, null=True, on_delete=models.SET_NULL)


class Courses(models.Model):
    name = models.CharField(max_length=32)
    num = models.IntegerField(default=1)


class Students(models.Model):
    name = models.CharField(max_length=32)
    course = models.ForeignKey(Courses, null=True, on_delete=models.SET_NULL)


class Orders(models.Model):
    date = models.DateTimeField(auto_now_add=True)

from django.db import models
from datetime import date

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name} ({self.id})'


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField('post date')
    details = models.CharField(max_length=2000)

    def __str__(self):
        return f'{self.title} ({self.id})'

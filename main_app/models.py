from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.title} ({self.id})'

from django.db import models

# Create your models here.
class todolist(models.Model):
    tittle = models.CharField(max_length=100)
    descraption = models.TextField()
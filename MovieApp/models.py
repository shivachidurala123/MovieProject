from django.db import models

# Create your models here.
class Movies(models.Model):
    releasedate=models.DateField();
    moviename=models.CharField(max_length=50);
    actor=models.CharField(max_length=50);
    actress=models.CharField(max_length=30);
    ratings=models.IntegerField();


from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.CharField(max_length=800, verbose_name='Description')
    rating = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], verbose_name='Rating')



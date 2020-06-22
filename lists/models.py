from django.db import models

# Create your models here.

class List(models.Model):
    '''Список'''
    pass

class Item(models.Model):
    list = models.ForeignKey(List, default='', on_delete=models.CASCADE)
    text = models.TextField(default='')
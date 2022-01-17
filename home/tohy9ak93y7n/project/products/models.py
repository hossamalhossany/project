from django.db import models
from datetime import datetime


# Create your models here.


class Product(models.Model):
    choise = [('phone', 'phone'), ('computer', 'computer')]
    name = models.CharField(max_length=50, default='please enter name', verbose_name='title')
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    active = models.BooleanField(default=True, verbose_name='act')
    category = models.CharField(max_length=50, verbose_name='cat.', null=True, blank=True, choices=choise)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Test(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    created = models.DateTimeField(null=True, default=datetime.now)

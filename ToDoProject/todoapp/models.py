from sys import float_repr_style
from django.db import models
from datetime import datetime
# Create your models here.

class Todos(models.Model):
    title=models.CharField(max_length=100, blank=False)
    description=models.TextField(max_length=1000,blank=True)
    urgent=models.BooleanField(default=False)
    done=models.BooleanField(default=False)
    create=models.DateTimeField(default=datetime.now, blank=True)
    endtime=models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
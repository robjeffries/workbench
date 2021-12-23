#from django.db import models
from djongo import models

# Create your models here.
class Log(models.Model):
    host            = models.CharField(max_length=15)
    log             = models.CharField(max_length=1)
    user            = models.CharField(max_length=1)
    time            = models.CharField(max_length=26)
    request_method  = models.CharField(max_length=20)
    request         = models.CharField(max_length=500)
    proto           = models.CharField(max_length=10)
    status          = models.CharField(max_length=3)
    bytes           = models.CharField(max_length=10)
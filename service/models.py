from django.db import models

# Create your models here.
class database(models.Model):
    name = models.CharField(max_length=255)
    accountNumber = models.CharField(max_length=255)
    pin = models.CharField(max_length=50)
    balance = models.IntegerField()
    def __str__(self):
        return self.name
    

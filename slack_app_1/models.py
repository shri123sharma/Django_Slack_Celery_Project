from django.db import models

# Create your models here.
class Company(models.Model):
    com_name=models.CharField(max_length=255,null=True, blank=True)
    
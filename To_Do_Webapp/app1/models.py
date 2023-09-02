from django.db import models


# Create your models here.


class To_Do_data(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
   

from django.db import models

# Create your models here.
class TableData(models.Model):
    data_1 = models.CharField(max_length=20)
    data_2 = models.CharField(max_length=20)

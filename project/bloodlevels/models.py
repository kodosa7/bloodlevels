from django.db import models
from datetime import datetime

class Date(models.Model):
    my_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.my_date)

class Level(models.Model):
    name = models.CharField(max_length=200)
    value = models.FloatField()
    unit = models.CharField(max_length=10)
    tolerance = models.CharField(max_length=10)
    date_id = models.ForeignKey(Date, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
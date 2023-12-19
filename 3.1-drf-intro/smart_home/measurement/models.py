from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()


class Measurement(models.Model):
    temperature = models.FloatField()
    time_created = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT,related_name='measurements')
    
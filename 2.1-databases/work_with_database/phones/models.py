from django.db import models


class Phone(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True, serialize=False)
    name = models.CharField(max_length=50)
    image = models.CharField()
    price = models.FloatField()
    release_date = models.DateTimeField()
    lte_exists = models.CharField(max_length=10)
    

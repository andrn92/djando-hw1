from django.db import models
from django.urls import reverse


class Phone(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True, serialize=False)
    name = models.CharField(max_length=50)
    image = models.CharField()
    price = models.FloatField()
    release_date = models.DateTimeField()
    lte_exists = models.CharField(max_length=10)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})
    

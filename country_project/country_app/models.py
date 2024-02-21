from django.db import models
from django.utils.text import slugify

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    slug = models.SlugField(max_length=10, unique=True, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:3].upper()
        super(Country, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class State(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=10, unique=True, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='states')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:3].upper()
        super(State, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=10, unique=True, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True, related_name='cities')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:3].upper()
        super(City, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

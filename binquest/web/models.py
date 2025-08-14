from django.db import models
from django.contrib.auth.models import User




class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.place} - {self.category}'
    


    def get_location_url(self):
        return f"https://maps.google.com/?q={self.latitude},{self.longitude}"
    


from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    name_lower = models.CharField(max_length=255, editable=False)
    genre = models.CharField(max_length=100)
    poster = models.CharField(max_length=255)
    description = models.TextField()
    
    def save(self, *args, **kwargs):
        self.name_lower = self.name.lower()
        super(Movie, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

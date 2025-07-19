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


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    text = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}: {self.text}'
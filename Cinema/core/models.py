from django.db import models
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Комментарии'
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.id}) {self.user.username}: {self.text}'
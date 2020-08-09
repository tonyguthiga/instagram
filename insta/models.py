from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'posts/', blank=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
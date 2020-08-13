from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(default=None, blank=True, upload_to = 'posts/')
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.caption)

    @classmethod
    def search_by_author(cls,author):
        authors = Post.objects.filter(author__author__icontains=author)
        return authors

    @classmethod
    def get_single_photo(cls,id):
        image = cls.objects.get(pk=id)
        return image

class Likes(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Post, blank=True, on_delete=models.CASCADE,related_name='comment')
    comment = models.CharField(max_length=150, blank=True)
    date_commented = models.DateTimeField(default=timezone.now)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    class Meta:
        ordering = ['-date_commented']

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image__id=id)
        return comments

    def __str__(self):
        return str(self.comment)
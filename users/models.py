from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=250)

    @receiver(post_save, sender=User)
    def create_profile_for_new_user(sender, created, instance, **kwargs):
        if created:
            profile = Profile(user=instance)
            profile.save()
    
    def __str__(self):
        return f'{self.user.username} Profile'

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_img = models.ImageField(null=True, blank=True, upload_to="profile_images/", default="../static/imgs/profile-image-default.png")
    slug = models.SlugField(unique=True, default='temp')
    bio = models.TextField(max_length=500, null=True, blank=True)
    reputation = models.IntegerField(default=0)
    post_count = models.PositiveIntegerField(default=0)
    topic_count = models.PositiveIntegerField(default=0)
    thread_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.slug == 'temp':
            self.slug = slugify(self.user.username)
        return super(UserProfile, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.user.username
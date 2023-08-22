from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.crypto import get_random_string

from django.utils.html import mark_safe
from markdown import markdown
# Create your models here.



class Topic(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Topic name', max_length=250)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    last_thread_date = models.DateTimeField(null=True, blank=True)
    # last_reply_date = models.DateTimeField()
    description = models.TextField('Topic description', max_length=500)
    slug = models.SlugField(unique=True, default='temp')
    thread_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if(self.slug=='temp'):
            self.slug = slugify(self.name)
        return super(Topic, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    def get_thread_count(self):
        return Thread.objects.filter(topic=self).count()
    
    def get_last_thread(self):
        return Thread.objects.filter(topic=self).order_by('-date_created').first()
    
class Thread(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE , related_name="threads")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="threads")
    name = models.CharField('Thread name', max_length=250)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    last_reply_date = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(unique=True, default='temp')
    view_count = models.PositiveIntegerField(default=0)
    post_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if(self.slug=='temp'):
            self.slug = slugify(self.name)
        return super(Thread, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    def get_last_post(self):
        return Post.objects.filter(thread=self).order_by('-date_created').first()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField('Post content', max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    like_count = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='liked_posts', null=True, blank=True)
    slug = models.SlugField(unique=True, default='temp')

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))

    def save(self, *args, **kwargs):
        if(self.slug=='temp'):
            unique_id = get_random_string(length=6)
            self.slug = slugify(self.thread.name + '-' + self.author.username + '-' + unique_id)
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug
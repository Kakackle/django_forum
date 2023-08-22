from django.contrib import admin
from users.models import UserProfile
from forum.models import Topic, Thread, Post

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Topic)
admin.site.register(Thread)
admin.site.register(Post)

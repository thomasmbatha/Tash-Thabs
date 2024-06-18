# Blog Models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to='photos/', default='default_image.jpg')
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_count = models.PositiveIntegerField(default=0)
    quotes = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'
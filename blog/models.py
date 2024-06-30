# blog/models.py
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.

class Bio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Bio"

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    living = models.BooleanField(default=False)
    bedroom = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    bathroom = models.BooleanField(default=False)
    outdoor = models.BooleanField(default=False)
    office = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.article}"
from django.contrib import admin
from .models import Article, Bio  # Import Bio model

# Register your models here.

admin.site.register(Article)
admin.site.register(Bio)  # Register Bio model

# blog/forms.py
from django import forms
from .models import Article, Comment, Bio

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'living', 'bedroom', 'kitchen', 'bathroom', 'outdoor', 'office']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = ['bio', 'profile_picture']

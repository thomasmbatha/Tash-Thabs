# blog/forms.py

from django import forms
from .models import Posts


class Posts(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['image','title','content','date_posted','author','comment_count','quotes','text']

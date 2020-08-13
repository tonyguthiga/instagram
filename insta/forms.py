 
from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','image','date_commented']

class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ['image', 'caption']
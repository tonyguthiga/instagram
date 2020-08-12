 
from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image', 'comment_owner']

class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ['image', 'caption']
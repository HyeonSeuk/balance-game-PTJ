from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('option1', 'image1', 'option2', 'image2',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
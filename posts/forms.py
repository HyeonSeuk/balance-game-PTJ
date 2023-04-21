from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    option1 = forms.CharField(
        label='Option1',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    image1 = forms.ImageField(
        label='Option1-이미지',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
            },
        ),
        required=False,
    )

    option2 = forms.CharField(
        label='Option2',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    image2 = forms.ImageField(
        label='Option2-이미지',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
            },
        ),
        required=False,
    )

    class Meta:
        model = Post
        fields = ('option1', 'image1', 'option2', 'image2',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    content = forms.CharField(
        widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'style' : 'width: 250px'
        }
        )
    )
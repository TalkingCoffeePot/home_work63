from django.forms import ModelForm, Textarea
from feed.models import PostModel, CommentModel
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = [
            'image',
            'text',

        ]
        widgets = {
            'text' : forms.Textarea(attrs={'placeholder': 'Описание', 'class': 'input_box text_box'}),
        }

class ReviewForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = [
            'author',
            'post_model',
            'text'
        ]
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Оставьте комментарий'
            })
        }
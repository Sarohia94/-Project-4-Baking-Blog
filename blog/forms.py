from .models import PostComment, RecipeComment
from django import forms


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('body',)


class RecipeCommentForm(forms.ModelForm):
    class Meta:
        model = RecipeComment
        fields = ('body',)

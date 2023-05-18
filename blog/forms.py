from .models import Post, Recipe, PostComment, RecipeComment
from django import forms


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('body',)


class RecipeCommentForm(forms.ModelForm):
    class Meta:
        model = RecipeComment
        fields = ('body',)


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "excerpt",
            "content",
        )


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "excerpt",
            "content",
        )

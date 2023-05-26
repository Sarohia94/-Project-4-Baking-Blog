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


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe

        readonly_fields = [
            'slug',
            'author',
        ]

        fields = [
            'recipe_name',
            'featured_image',
            'description',
            'serves',
            'prep_time',
            'baking_time',
            'ingredients',
            'special_equipment',
            'method',
            'bakers_tip',
        ]

        labels = {
            'recipe_name': 'Recipe Title',
            'featured_image': 'Recipe Image',
            'description': 'Description',
            'serves': 'Serves',
            'prep_time': 'Prep Time',
            'baking_time': 'Baking Time',
            'ingredients': 'Ingredients',
            'special_equipment': 'Special Equipment',
            'method': 'Method',
            'bakers_tip': 'BAKERS TIP',
        }

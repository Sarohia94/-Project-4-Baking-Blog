from django.contrib import admin
from .models import Post, PostComment, Recipe, RecipeComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Add fields to posts which will use summernote in admin panel
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'title', 'created_on')
    summernote_fields = ('content')


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    """
    Add fields for comments in admin panel & admin ability to approve comments
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    summernote_fields = ('content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Add fields for recipe which will use summernote in admin panel
    """
    list_display = ('recipe_name', 'slug', 'status', 'created_on')
    search_fields = ['recipe_name', 'method', 'ingredients']
    list_filter = ('status', 'recipe_name', 'created_on')


@admin.register(RecipeComment)
class RecipeCommentAdmin(admin.ModelAdmin):
    """
    Add fields for recipe comments in admin panel &
    admin ability to approve comments
    """
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    summernote_fields = ('content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

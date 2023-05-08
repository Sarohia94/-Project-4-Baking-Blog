from django.contrib import admin
from .models import Post, Comment, Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'title', 'created_on')
    summernote_fields = ('content')
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    summernote_fields = ('content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('recipe_name', 'slug', 'status', 'created_on')
    search_fields = ['recipe_name', 'method', 'ingredients']
    prepopulated_fields = {'slug': ('recipe_name',)}
    list_filter = ('status', 'recipe_name', 'created_on')
    actions = ['approve_recipe']

    def approve_recipe(self, request, queryset):
        queryset.update(approved=True)

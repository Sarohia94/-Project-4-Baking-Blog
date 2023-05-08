from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=80, verbose_name=('Recipe name'))
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe_posts'
    )
    description = models.TextField(max_length=500, blank=True)
    slug = models.SlugField(unique=True, max_length=80)
    serves = models.IntegerField(blank=True)
    prep_time = models.CharField(max_length=15)
    baking_time = models.CharField(max_length=15)
    ingredients = models.CharField(max_length=250)
    special_equipment = models.CharField(max_length=150, blank=True)
    method = models.TextField()
    bakers_tip = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.recipe

    def number_of_likes(self):
        return self.likes.count()

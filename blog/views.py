from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic, View
from django.views.generic import CreateView, DeleteView, UpdateView
from django.http import HttpResponseRedirect
from .models import Post, Recipe
from .forms import PostCommentForm, RecipeCommentForm, RecipeForm
from django.utils.text import slugify


class PostList(generic.ListView):
    """
    Render the blog home page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 4


class PostDetail(View):
    """
    Render the blog post detail page
    """
    def get(self, request, slug):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        post_comments = post.post_comments.filter(approved=True).order_by(
            "-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = {
                "post": post,
                "post_comments": post_comments,
                "commented": False,
                "liked": liked,
                "post_comment_form": PostCommentForm()
            }
        return render(request, "post_detail.html", context)

    def post(self, request, slug):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        post_comments = post.post_comments.filter(approved=True).order_by(
            "-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        post_comment_form = PostCommentForm(data=request.POST)
        if post_comment_form.is_valid():
            post_comment_form.instance.email = request.user.email
            post_comment_form.instance.name = request.user.username
            post_comment = post_comment_form.save(commit=False)
            post_comment.post = post
            post_comment.save()
        else:
            post_comment_form = PostCommentForm()
        context = {
                "post": post,
                "post_comments": post_comments,
                "commented": True,
                "liked": liked,
                "post_comment_form": PostCommentForm()
            }
        return render(request, "post_detail.html", context)


class RecipeList(generic.ListView):
    """
    Render the recipe page
    """
    model = Recipe
    queryset = Recipe.objects.all().order_by("-created_on")
    template_name = "recipes.html"
    paginate_by = 4


class RecipeDetail(View):
    """
    Render the recipe detail page
    """
    def get(self, request, slug):
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        recipe_comments = recipe.recipe_comments.filter(
            approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = {
                "recipe": recipe,
                "recipe_comments": recipe_comments,
                "commented": False,
                "liked": liked,
                "recipe_comment_form": RecipeCommentForm()
            }
        return render(request, "recipe_detail.html", context)

    def post(self, request, slug):
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        recipe_comments = recipe.recipe_comments.filter(
            approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        recipe_comment_form = RecipeCommentForm(data=request.POST)
        if recipe_comment_form.is_valid():
            recipe_comment_form.instance.email = request.user.email
            recipe_comment_form.instance.name = request.user.username
            recipe_comment = recipe_comment_form.save(commit=False)
            recipe_comment.recipe = recipe
            recipe_comment.save()
        else:
            recipe_comment_form = RecipeCommentForm()
        context = {
            "recipe": recipe,
            "recipe_comments": recipe_comments,
            "commented": False,
            "liked": liked,
            "recipe_comment_form": RecipeCommentForm()
        }
        return render(request, "recipe_detail.html", context)


class PostLike(View):
    """
    When a post is liked/unliked, the slug is noted
    and the like/unlike is counted. Total likes displayed.
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class RecipeLike(View):
    """
    When a recipe is liked/unliked, the slug is noted
    and the like/unlike is counted. Total likes displayed.
    """
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=self.request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        return HttpResponseRedirect(reverse("recipe_detail", args=[slug]))


class User(generic.ListView):
    """
    Render the user page
    """
    model = Recipe
    template_name = "user_page.html"


class AddRecipe(LoginRequiredMixin, CreateView):
    """
    Add recipe only when user is logged in,
    success message once submitted.
    """
    model = Recipe
    form_class = RecipeForm
    template_name = "add_recipe.html"
    success_url = "/recipes/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.recipe_name)
        messages.success(self.request, "Your recipe has been submitted!")
        return super(AddRecipe, self).form_valid(form)


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit recipe user has created, only when they are logged in,
    success message once updated.
    """
    model = Recipe
    form_class = RecipeForm
    template_name = "edit_recipe.html"
    success_url = "/recipes/"

    def form_valid(self, form):
        messages.success(self.request, "Your recipe has been updated!")
        return super(EditRecipe, self).form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().author


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete recipe user has created, only when they are logged in,
    success message once updated.
    """
    model = Recipe
    template_name = "delete_recipe.html"
    success_url = "/recipes/"
    success_message = "Post was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeleteRecipe, self).delete(request, *args, **kwargs)

    def test_func(self):
        return self.request.user == self.get_object().author

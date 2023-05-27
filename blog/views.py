from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic, View
from django.views.generic import CreateView, DeleteView, UpdateView
from django.http import HttpResponseRedirect
from .models import Post, Recipe
from .forms import PostCommentForm, RecipeCommentForm, RecipeForm
from django.utils.text import slugify


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 4


class PostDetail(View):
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
    model = Recipe
    queryset = Recipe.objects.all().order_by("-created_on")
    template_name = "recipes.html"
    paginate_by = 4


class RecipeDetail(View):
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
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class RecipeLike(View):
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=self.request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        return HttpResponseRedirect(reverse("recipe_detail", args=[slug]))


class User(generic.ListView):
    model = Recipe
    template_name = "user_page.html"


class AddRecipe(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "add_recipe.html"
    success_url = "/recipes/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.recipe_name)
        return super(AddRecipe, self).form_valid(form)


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "edit_recipe.html"
    success_url = "/recipes/"

    def test_func(self):
        return self.request.user == self.get_object().author


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = "delete_recipe.html"
    success_url = "/recipes/"

    def test_func(self):
        return self.request.user == self.get_object().author

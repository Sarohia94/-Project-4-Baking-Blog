from . import views
from .views import DeleteRecipe
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("recipes/", views.RecipeList.as_view(), name="recipes"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('recipes/<slug:slug>/', views.RecipeDetail.as_view(),
         name='recipe_detail'),
    path('post_like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('recipe_like/<slug:slug>', views.RecipeLike.as_view(),
         name='recipe_like'),
    path("user_page", views.User.as_view(), name="user_page"),
    path("add_recipe", views.AddRecipe.as_view(), name="add_recipe"),
    path("delete/<slug:slug>/", DeleteRecipe.as_view(), name="delete_recipe"),
]

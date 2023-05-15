from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("recipes", views.RecipeList.as_view(), name="recipes"),
    path('recipes/<slug:slug>/', views.RecipeDetail.as_view(),
         name='recipe_detail'),
]

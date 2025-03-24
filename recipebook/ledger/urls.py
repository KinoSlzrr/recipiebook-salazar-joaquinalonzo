from django.urls import path

from .views import RecipeListView, RecipeDetailView, RecipeCreateView


urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name="recipes-list"),
    path('recipes/create', RecipeCreateView.as_view(), name="recipe-create"),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name="recipe-detail")
]


app_name = "ledger"

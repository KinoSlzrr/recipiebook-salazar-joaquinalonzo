from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = 'home/recipes_list.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'home/recipe_base.html'

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe, RecipeIngredient

class RecipeListView(ListView):
    model = Recipe
    template_name = 'home/recipes_list.html'

class RecipeDetailView(DetailView):
    model = RecipeIngredient
    template_name = 'home/recipe_base.html'

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'home/recipes_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'home/recipe_detail.html'
    redirect_field_name = 'accounts/login'


class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'home/recipe_add.html'
    redirect_field_name = 'accounts/login'
    form_class = RecipeForm


class RecipeImageCreateView(CreateView):
    model = RecipeImage
    template_name = 'home/recipe_add_image.html'
    redirect_field_name = 'accounts/login'
    form_class = RecipeImageForm

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe

'''
    We're using master_context so we can just pull from it 
    instead of copy/pasting full context blocks
'''
master_context = {
        "recipes": [
            {
                "name": "Recipe 1",
                "ingredients": [
                    {
                        "name": "tomato",
                        "quantity": "3pcs"
                    },
                    {
                        "name": "onion",
                        "quantity": "1pc"
                    },
                    {
                        "name": "pork",
                        "quantity": "1kg"
                    },
                    {
                        "name": "water",
                        "quantity": "1L"
                    },
                    {
                        "name": "sinigang mix",
                        "quantity": "1 packet"
                    }
                ],
                "link": "/recipe/1"
            },
            {
                "name": "Recipe 2",
                "ingredients": [
                    {
                        "name": "garlic",
                        "quantity": "1 head"
                    },
                    {
                        "name": "onion",
                        "quantity": "1pc"
                    },
                    {
                        "name": "vinegar",
                        "quantity": "1/2cup"
                    },
                    {
                        "name": "water",
                        "quantity": "1 cup"
                    },
                    {
                        "name": "salt",
                        "quantity": "1 tablespoon"
                    },
                    {
                        "name": "whole black peppers",
                        "quantity": "1 tablespoon"
                    },
                    {
                        "name": "pork",
                        "quantity": "1 kilo"
                    }
                ],
                "link": "/recipe/2"
            }
        ]
    }

class RecipeListView(ListView):
    model = Recipe
    template_name = 'home/recipes_list.html'

def index(request):
    return HttpResponse('Hello World!')

def recipes_list(request):
    ctx = master_context
    return render(request, 'recipes_list.html', ctx)

'''
    We use the same html file since the only thing that changes
    between the two different pages is the data
'''
def recipe_1(request):
    ctx = master_context["recipes"][0]
    return render(request, 'recipe_base.html', ctx)

def recipe_2(request):
    ctx = master_context["recipes"][1]
    return render(request, 'recipe_base.html', ctx)


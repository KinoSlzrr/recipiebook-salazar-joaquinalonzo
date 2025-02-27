from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home:recipe_base', args=[self.pk])

class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:recipes-list', args=[self.pk])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.SET_NULL,
        null = True,
        related_name = 'ingredients',
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete = models.SET_NULL,
        null = True,
        related_name = 'recipes',
    )



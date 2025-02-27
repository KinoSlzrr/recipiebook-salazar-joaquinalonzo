from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    quantity = models.IntegerField()

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



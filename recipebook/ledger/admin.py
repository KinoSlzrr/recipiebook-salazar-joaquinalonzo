from django.contrib import admin

from .models import Recipe, RecipeIngredient, Ingredient

class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    inlines = [RecipeIngredientInLine,]

admin.site.register(Recipe, RecipeIngredientAdmin)

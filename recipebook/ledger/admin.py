from django.contrib import admin

from .models import Recipe, RecipeIngredient

class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inline = [RecipeIngredientInLine,]


admin.site.register(Recipe, RecipeAdmin)

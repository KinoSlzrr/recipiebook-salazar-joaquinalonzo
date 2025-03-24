from django.contrib import admin

from .models import Recipe, RecipeIngredient, RecipeImage


class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    inlines = [
        RecipeIngredientInLine,
        RecipeImageInLine
    ]


admin.site.register(Recipe, RecipeIngredientAdmin)

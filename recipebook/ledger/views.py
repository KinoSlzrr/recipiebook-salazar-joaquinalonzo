from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import redirect

from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'home/recipes_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'home/recipe_detail.html'
    redirect_field_name = 'accounts/login'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'home/recipe_add.html'
    redirect_field_name = 'accounts/login'
    form_class = RecipeForm


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = 'home/recipe_add_image.html'
    redirect_field_name = 'accounts/login'
    form_class = RecipeImageForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        ctx['pk'] = pk
        ctx['recipe'] = Recipe.objects.get(pk=pk)
        ctx['form'] = RecipeImageForm()
        return ctx

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        form = RecipeImageForm(request.POST, request.FILES)

        if form.is_valid():
            r = RecipeImage()
            r.image = request.FILES.get('image')
            r.recipe = Recipe.objects.get(pk=pk)

            r.save()
            return redirect(reverse('ledger:recipe-detail', args=[pk]))
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

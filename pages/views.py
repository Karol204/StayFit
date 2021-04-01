import random

from django.shortcuts import render
from django.views import View

from pages.models import Recipe


class LandingView(View):

    def get(self, request):
        all_recipe = list(Recipe.objects.all())
        random.shuffle(all_recipe)
        first = all_recipe[0]
        second = all_recipe[1]
        third = all_recipe[2]
        ctx = {
            'all_recipe': all_recipe,
            'first': first,
            'second': second,
            'third': third
        }
        return render(request, 'index.html', ctx)


class Dashboard(View):

    def get(self, request):
        return render(request, 'dashboard.html')
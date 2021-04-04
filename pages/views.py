import random

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from pages.models import Recipe, Plan, RecipePlan, DayName


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

        plans = Plan.objects.all()
        recipes = Recipe.objects.all()
        number_of_recipes = recipes.count()
        numer_of_plans = plans.count()

        plans_list = list(plans)
        plans_list.sort(key=lambda created:created)
        last_added_plan = plans_list[0]
        recipe_in_plan = RecipePlan.objects.filter(plan=last_added_plan)
        recipe_in_plan = recipe_in_plan.order_by('day_name')



        ctx = {
            'numer_of_plans': numer_of_plans,
            'number_of_recipes': number_of_recipes,
            'last_added_plan': last_added_plan,
            'recipe_in_plan': recipe_in_plan
        }
        return render(request, 'dashboard.html', ctx)


class RecipeList(View):

    def get(self, request):
        all_recipes = Recipe.objects.all().order_by('votes')
        ctx = {
            'all_recipes': all_recipes,
        }
        return render(request, 'app-recipes.html', ctx)


class RecipeAdd(View):

    def get(self, request):
        return render(request, 'app-add-recipe.html')

    def post(self, request):
        recipe_name = request.POST.get('recipeName')
        recipe_description = request.POST.get('recipeDescription')
        prep_time = request.POST.get('prepTime')
        preparation = request.POST.get('preparation')
        ingredients = request.POST.get('ingredients')
        try:
            new_recipe = Recipe()
            new_recipe.name = recipe_name
            new_recipe.description = recipe_description
            new_recipe.preparation_time = prep_time
            new_recipe.preparation = preparation
            new_recipe.ingredients = ingredients
            new_recipe.save()
            return redirect('/recipe/list')
        except:
            ctx = {
                'error': True,
                'errorMessage': 'Cos poszlo nie tak'
            }
            return JsonResponse(ctx)



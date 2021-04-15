import random

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from pages.forms import PlanRecipeForm
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
        # plans_list.sort(key=lambda created: created)
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


class RecipeDetails(View):

    def get(self, request, id):
        recipe = Recipe.objects.get(pk=id)
        recipe_ing = recipe.ingredients
        ingredients = recipe_ing.split(', ')
        ctx = {
            'recipe': recipe,
            'ingredients': ingredients,
        }
        return render(request, 'app-recipe-details.html', ctx)

class PlanList(View):

    def get(self, request):
        plans = Plan.objects.all().order_by('id')
        print(plans)
        ctx = {
            'plans': plans,
        }
        return render(request, 'app-schedules.html', ctx)


class PlanAdd(View):

    def get(self, request):
        ctx = {

        }
        return render(request, 'app-add-schedules.html', ctx)

    def post(self, request):
        plan_name = request.POST.get('planName')
        plan_description = request.POST.get('planDescription')

        try:
            new_plan = Plan()
            new_plan.name = plan_name
            new_plan.description = plan_description
            new_plan.save()
            ctx = {
                'error': True,
                'errorMessage': 'Plan dodany pomyslnie'
            }
            return JsonResponse(ctx)
        except:
            ctx = {
                'error': True,
                'errorMessage': 'Cos poszlo nie tak'
            }
            return JsonResponse(ctx)

class PlanDetails(View):

    def get(self, request, id):
        plan = Plan.objects.get(pk=id)
        all_recipe = RecipePlan.objects.filter(plan=plan)
        ctx = {
            'plan': plan,
            'all_recipe': all_recipe
        }
        return render(request, 'app-details-schedules.html', ctx)


class AddRecipeToPlan(View):

    def get(self, request):
        form = PlanRecipeForm()
        ctx ={
            'form':form,
        }
        return render(request, 'app-schedules-meal-recipe.html', ctx)

    def post(self, request):
        chosen_plan_id = request.POST.get('chosenPlan')
        chosen_meal = request.POST.get('chosenMeal')
        meal_order = request.POST.get('mealNumber')
        recipe_id = request.POST.get('recipe')
        day_name_id = request.POST.get('dayName')

        chosen_plan = Plan.objects.get(pk=chosen_plan_id)
        recipe = Recipe.objects.get(pk=recipe_id)
        day_name = DayName.objects.get(pk=day_name_id)



        print(chosen_plan)
        print(chosen_meal)
        print(meal_order)
        print(recipe)
        print(day_name)

        try:
            new_recipe_in_plan = RecipePlan()
            new_recipe_in_plan.meal_name = chosen_meal
            new_recipe_in_plan.plan = chosen_plan
            new_recipe_in_plan.order = meal_order
            new_recipe_in_plan.day_name = day_name
            new_recipe_in_plan.recipe = recipe
            new_recipe_in_plan.save()
            ctx = {
                'error': True,
                'errorMessage': 'Przepis dodano do planu'
            }
            return JsonResponse(ctx)
        except:
            ctx = {
                'error': True,
                'errorMessage': 'Cos poszlo nie tak, sprobuj ponownie pozniej'
            }
            return JsonResponse(ctx)


def recipe_like(request):
    recipe_id = request.POST.get('recipeId')
    recipe = Recipe.objects.get(pk=recipe_id)
    likes = int(recipe.votes)
    likes += 1
    recipe.votes = likes
    recipe.save()
    ctx = {
        'error': True,
        'errorMessage': 'Przepis dodano do planu'
    }
    return JsonResponse(ctx)

def recipe_dislike(request):
    recipe_id = request.POST.get('recipeId')
    recipe = Recipe.objects.get(pk=recipe_id)
    likes = int(recipe.votes)
    likes -= 1
    recipe.votes = likes
    recipe.save()
    ctx = {
        'error': True,
        'errorMessage': 'Przepis dodano do planu'
    }
    return JsonResponse(ctx)

def recipe_delete(request, id):
    recipe = Recipe.objects.get(pk=id)
    recipe.delete()
    return redirect('/recipe/list')

def plan_delete(request, id):
    plan = Plan.objects.get(pk=id)
    plan.delete()
    return redirect('/plan/list')
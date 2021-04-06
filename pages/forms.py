from django.forms import forms, ModelForm

from pages.models import RecipePlan


class PlanRecipeForm(ModelForm):

    class Meta:
        model = RecipePlan
        exclude = []
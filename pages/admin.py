from django.contrib import admin
from .models import Recipe, Plan, DayName, RecipePlan
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Plan)
admin.site.register(RecipePlan)
admin.site.register(DayName)
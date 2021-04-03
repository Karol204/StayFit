from enum import Enum, IntEnum

from django.db import models

# Create your models here.

WeekDay = (
        ('Monday', 1),
        ('Tuesday',  2),
        ('Wednesday',  3),
        ('Thursday',  4),
        ('Friday',  5),
        ('Saturday', 6),
        ('Sunday',  7),
     )

class Recipe(models.Model):
    name = models.CharField(max_length=250)
    ingredients = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    created = models.DateField(auto_now_add=True)
    preparation_time = models.IntegerField()
    votes = models.IntegerField(default=0)


class Plan(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.description}'


class DayName(models.Model):

    name = models.CharField(max_length=16)
    order = models.CharField(choices=WeekDay, max_length=15)

    def __str__(self):
        return f'{self.name}'


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    order = models.IntegerField()
    day_name = models.ForeignKey(DayName, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.meal_name} {self.day_name} {self.plan}'
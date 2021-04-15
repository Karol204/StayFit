from django.contrib import admin
from django.urls import path

from pages.views import LandingView, Dashboard, PlanAdd, recipe_dislike, AddRecipeToPlan, RecipeList, PlanList, \
    RecipeAdd, PlanDetails, RecipeDetails, recipe_like, recipe_delete, plan_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingView.as_view(), name='home'),
    path('main/', Dashboard.as_view()),
    path('recipe/<int:id>', RecipeDetails.as_view()),
    path('recipe/list/', RecipeList.as_view()),
    path('recipe/add/', RecipeAdd.as_view()),
    path('recipe/delete/<int:id>', recipe_delete),
    # path('recipe/modify/<int:id>', ),
    path('plan/list/', PlanList.as_view()),
    path('plan/add/', PlanAdd.as_view()),
    path('plan/<int:id>/', PlanDetails.as_view()),
    path('plan/add-recipe/', AddRecipeToPlan.as_view()),
    path('plan/like/', recipe_like),
    path('plan/dislike/', recipe_dislike),
    path('plan/delete/<int:id>', plan_delete),

]

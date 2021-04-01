from django.contrib import admin
from django.urls import path

from pages.views import LandingView, Dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingView.as_view(), name='home'),
    path('main/', Dashboard.as_view()),
    # path('recipe/<int:id>', ),
    # path('recipe/list/', ),
    # path('recipe/add/', ),
    # path('recipe/modify/<int:id>', ),
    # path('plan/add/', ),
    # path('plan/add-recipe/', )
]

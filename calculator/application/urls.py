from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator, name='calculator'),  # Route for the calculator page
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator2, name='calculator2'),  # Route for the calculator page
]

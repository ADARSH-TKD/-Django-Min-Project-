from django.shortcuts import render
from django.http import HttpRenspose
# Create your views here.
def index(request):
    return render("index.html")
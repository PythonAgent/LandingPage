from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='main/home.html')

def admin(request):
    return render(request = request,
                  template_name='main/dashboard.html')

def teacher(request):
    return render(request = request,
                  template_name='main/teacher.html')

def tutorials(request):
    return render(request = request,
                  template_name='main/tutorials.html')


def library(request):
    return render(request = request,
                  template_name='main/library.html')


def tutorialsSeries(request):
    return render(request = request,
                  template_name='main/tutorialsSeries.html')
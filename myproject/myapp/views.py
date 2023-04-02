from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee


# Create your views here.
def index(request):
    return HttpResponse("Home Page")

def test_plotly_app(request):
    return render(request, 'plotly_app.html')

def dash_layout(request):
    return render(request, 'dash_layout.html')

def web_layout(request):
    return render(request, 'web_layout.html')

def responsive_layout(request):
    return render(request, 'responsive_layout.html')

def bootstrap_examples(request):
    return render(request, 'bootstrap_examples.html')

def get_employee_details(request):
    return render(request, 'emp_details.html')
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Home Page")

def test_plotly_app(request):
    return render(request, 'plotly_app.html')

def dash_layout(request):
    return render(request, 'dash_layout.html')

def web_layout(request):
    return render(request, 'web_layout.html')
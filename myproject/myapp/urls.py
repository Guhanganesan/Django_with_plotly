from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('plotly_app', views.test_plotly_app)
]
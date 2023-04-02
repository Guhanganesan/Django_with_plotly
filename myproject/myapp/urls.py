from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('plotly_app', views.test_plotly_app),
    path('dash_layout', views.dash_layout),
    path('web_layout', views.web_layout),
    path('responsive_layout', views.responsive_layout),
    path('bootstrap_examples', views.bootstrap_examples),
    path('employee-details', views.get_employee_details)
]
# Django Installations
1. python -m venv env
2. env\Scripts\activate
3. pip install django
4. django-admin startproject myproject
5. cd myproject
6. python manage.py startapp myapp
7. python manage.py migrate
8. python manage.py runserver
9. open in browser: http://127.0.0.1:8000/

# Django Plotly Installations

1. pip install django_plotly_dash
2. open settings.py file and add 'django_plotly_dash.apps.DjangoPlotlyDashConfig' in INSTALLED_APPS 
3. Also add myapp in same INSTALLED_APPS 
4. And add => X_FRAME_OPTIONS = 'SAMEORIGIN' in same settings.py file
5. And add => path('django_plotly_dash/', include('django_plotly_dash.urls')) in project urls
6. from django.urls import path, include
7. Run again => python manage.py migrate

Reference: https://django-plotly-dash.readthedocs.io/en/latest/installation.html
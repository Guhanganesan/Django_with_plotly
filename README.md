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

Or
8. python manage.py makemigrations
9. python manage.py migrate

Reference: https://django-plotly-dash.readthedocs.io/en/latest/installation.html

# Sample Example

import dash
from dash import dcc, html

from django_plotly_dash import DjangoDash

app = DjangoDash('SimpleExample')   # replaces dash.Dash

app.layout = html.Div([
    dcc.RadioItems(
        id='dropdown-color',
        options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
        value='red'
    ),
    html.Div(id='output-color'),
    dcc.RadioItems(
        id='dropdown-size',
        options=[{'label': i,
                  'value': j} for i, j in [('L','large'), ('M','medium'), ('S','small')]],
        value='medium'
    ),
    html.Div(id='output-size')

])

@app.callback(
    dash.dependencies.Output('output-color', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value')])
def callback_color(dropdown_value):
    return "The selected color is %s." % dropdown_value

@app.callback(
    dash.dependencies.Output('output-size', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value'),
     dash.dependencies.Input('dropdown-size', 'value')])
def callback_size(dropdown_color, dropdown_size):
    return "The chosen T-shirt is a %s %s one." %(dropdown_size,
                                                  dropdown_color)

Link: https://django-plotly-dash.readthedocs.io/en/latest/simple_use.html

# Dash Layout 
1. Install Pandas: pip install pandas

Example link : https://dash.plotly.com/layout

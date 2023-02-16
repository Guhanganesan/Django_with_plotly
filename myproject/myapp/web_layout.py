# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash

app = DjangoDash('WebLayout')

container = {
        'border':'2px solid green',
        'width': '1200px',
        'height':'800px'
    }

left_side = {
        'border':'2px solid blue',
        'width': '400px',
        'height':'796px',
        'float':'left'
    }

right_side = {
        'border':'2px solid red',
        'width': '790px',
        'height':'796px',
        'float':'left'
    }

left_side_top = {
        'border':'2px solid green',
        'width': '398px',
        'height':'390px'
    }

left_side_bottom = { #can change if you need
        'border':'2px solid green',
        'width': '398px',
        'height':'390px'
    }

app.layout = html.Div(
    style=container, 
    children=[

        html.Div(
            style=left_side,
            children=[
                html.Div(
                    style=left_side_top,
                    children=["Left Side Top"]
                ),
                html.Div(
                    style=left_side_bottom,
                    children=["Left Side Bottom"]
                ),

            ]
        ),

        html.Div(
            style=right_side,
            children=["Right"]
        )

])

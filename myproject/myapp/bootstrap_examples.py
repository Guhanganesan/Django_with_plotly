from dash import Dash, dcc, html
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

app = DjangoDash('BootstrapExamples')

app.layout = dbc.DropdownMenu(
    label="Menu",
    children=[
        dbc.DropdownMenuItem("Item 1"),
        dbc.DropdownMenuItem("Item 2"),
        dbc.DropdownMenuItem("Item 3"),
    ],
) 

app.css.append_css({
    "external_url": "https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)
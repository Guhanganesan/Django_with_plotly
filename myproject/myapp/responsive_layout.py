from dash import Dash, dcc, html
from django_plotly_dash import DjangoDash

app = DjangoDash('Responsive')

app.layout = html.Div(
    className="container",
    children=[

        # For Testing Header Parts
        html.Div(
            className="jumbotron text-center",
            children=[
                html.H1(
                    "My First Bootstrap Page"
                ),
                html.P(
                    "Resize this responsive page to see the effect!"
                )
            ]
        ),

        #--- For Row -----#
        html.Div(
            className="row",
            children=[
                # Inside Row with different columns
                html.Div(
                    className="col-sm-4",
                    children=[
                        "Bootstrap 5 is the newest version of Bootstrap; with new components, faster stylesheets, more responsiveness etc. It supports the latest, stable releases of all major browsers and platforms. However, Internet Explorer 11 and down is not supported."
                    ]
                ),

                html.Div(
                    className="col-sm-4",
                    children=[
                        "Bootstrap 5 is the newest version of Bootstrap; with new components, faster stylesheets, more responsiveness etc. It supports the latest, stable releases of all major browsers and platforms. However, Internet Explorer 11 and down is not supported."
                    ]
                ),
                
                html.Div(
                    className="col-sm-4",
                    children=[
                        "Bootstrap 5 is the newest version of Bootstrap; with new components, faster stylesheets, more responsiveness etc. It supports the latest, stable releases of all major browsers and platforms. However, Internet Explorer 11 and down is not supported."
                    ]
                )
            ]
        )
    ]
)

app.css.append_css({
    "external_url": "https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)
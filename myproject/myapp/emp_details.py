import psycopg2
import pandas as pd
import dash
from dash import Dash, html, Input, Output, dcc, dash_table 
from django_plotly_dash import DjangoDash

from .models import Employee

app = DjangoDash('EmployeeDetails') 

app.layout = html.Div(
     id="title",
    children=[
        html.H1("Employee Details"),
        dcc.Dropdown(
            id="my_dpdn",
            options=[
                {"label":x, "value":x} for x in [1,2,3,4,5]
            ]
        ),
        dash_table.DataTable(
            id="my_table_id",
            sort_action='native',
            columns=[
                {'name': 'id', 'id': 'id'},
                {'name': 'EmpId', 'id': 'EmpId'},
                {'name': 'EmpName', 'id': 'EmpName'},
                {'name': 'EmpGender', 'id': 'EmpGender'},
                {'name': 'EmpEmail', 'id': 'EmpEmail'},
                {'name': 'EmpDesignation', 'id': 'EmpDesignation'},
            ],
            editable=True,
        ),
    ],
    style={
        "width":"200px"
    }
)


@app.callback(
    Output(
        "my_table_id", "data"
    ),
    Input(
        "my_dpdn", "value"
    )
)
def get_dropdown_value(value):
    try:
        if value:
            employees = Employee.objects.filter(id=int(value)).values()
            print(employees)
            table_data = {}
            employee_list = []
            for person in employees:
                table_data = person
            
            employee_list.append(table_data)
            return employee_list
        
    except Exception as e:
        return e  


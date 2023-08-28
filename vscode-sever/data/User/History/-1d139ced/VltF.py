# Import packages
from dash import Dash, html, callback, Output, Input, State
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = html.Div ([
    html.H6 ("Predict the car price based on the data you entered:")
])

app.layout = dbc.Container([
    dbc.Row([
        
    ])
    dbc.Row([
        html.Div([
            dbc.Label("Feature1: Engine"),
            dbc.Input(id="x_1", type="number", placeholder="Put a value for x_1"),
            dbc.Label("Feature2: Year"),
            dbc.Input(id="x_2", type="number", placeholder="Put a value for x_2"),
            dbc.Button(id="submit", children="calculate y", color="primary", className="me-1"),
            dbc.Label("Predicted Car Price based on your data is: "),
            html.Output(id="y", children="")
        ],
        className="mb-3")
    ])

], fluid=True)

@callback(
    Output(component_id="y", component_property="children"),
    State(component_id="x_1", component_property="value"),
    State(component_id="x_2", component_property="value"),
    Input(component_id="submit", component_property='n_clicks'),
    prevent_initial_call=True
)
def calculate_y(x_1, x_2, submit):
    return x_1 + x_2
# Run the app
if __name__ == '__main__':
    app.run(debug=True)

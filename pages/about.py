from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.H2("About The Developer", className="mb-4 text-info fw-bold"),
    html.P("I am a Data Analyst passionate about turning raw data into actionable insights.", className="lead"),
    dbc.Button("GitHub", href="#", color="dark", className="me-2"),
    dbc.Button("LinkedIn", href="#", color="primary")
], className="py-4 text-center")

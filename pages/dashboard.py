from dash import html, dcc
import dash_bootstrap_components as dbc
from data.data_loader import load_data
from utils.visualizations import generate_graphs

df, df_under_60 = load_data()
figs = generate_graphs(df, df_under_60)

if not figs:
    layout = html.Div(html.H3("⚠️ Please add the CSV file to the 'data' folder.", className="text-danger text-center mt-5"))
else:
    layout = dbc.Container([
        html.H2("Interactive Dashboard", className="mb-4 text-primary fw-bold"),
        dbc.Row([
            dbc.Col(dcc.Graph(figure=figs['user_type']), md=6),
            dbc.Col(dcc.Graph(figure=figs['gender']), md=6),
        ], className="mb-4"),
        dbc.Row([
            dbc.Col(dcc.Graph(figure=figs['top_start']), md=12),
        ], className="mb-4"),
        dbc.Row([
            dbc.Col(dcc.Graph(figure=figs['box']), md=12),
        ])
    ], fluid=True, className="py-4")

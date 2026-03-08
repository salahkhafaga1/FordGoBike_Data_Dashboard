from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Ford GoBike Analytics", className="display-4 fw-bold text-primary mb-3"),
            html.P("Explore comprehensive insights into bike-sharing usage patterns across the San Francisco Bay Area in 2019.", className="lead text-muted mb-4"),
            dbc.Button("Go to Dashboard", href="/dashboard", color="primary", size="lg", className="me-2"),
            dbc.Button("View Insights", href="/insights", color="outline-secondary", size="lg"),
        ], md=8, className="py-5 mx-auto text-center")
    ], align="center", className="py-5")
], fluid=True)

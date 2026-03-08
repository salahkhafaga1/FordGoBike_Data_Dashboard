from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.H2("💡 Key Business Recommendations", className="mb-4 text-success fw-bold"),
    dbc.Card([
        dbc.CardBody([
            html.H5("1. Optimize Fleet Rebalancing", className="fw-bold"),
            html.P("Ensure maximum bike availability at the Top 10 Start/End stations during peak commuting hours.", className="text-muted"),
            html.Hr(),
            html.H5("2. Convert Customers to Subscribers", className="fw-bold"),
            html.P("Introduce a 'Weekend Pass' or 'Tourist Subscription' to capture more value from casual riders who take longer trips.", className="text-muted"),
        ])
    ], className="shadow-sm border-left-success")
], className="py-4")

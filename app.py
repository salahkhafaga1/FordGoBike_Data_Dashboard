import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
from pages import home, dashboard, insights, about

# Initialize the app with a Bootstrap theme
# LUX بيدي شكل احترافي جداً وخطوط عريضة شيك
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX], suppress_callback_exceptions=True)
app.title = "Ford GoBike App"

# Navbar Setup
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Dashboard", href="/dashboard")),
        dbc.NavItem(dbc.NavLink("Insights", href="/insights")),
        dbc.NavItem(dbc.NavLink("About Me", href="/about")),
    ],
    brand="🚴‍♂️ Ford GoBike",
    brand_href="/",
    color="primary",
    dark=True,
    className="mb-4"
)

# App Layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content', style={'minHeight': '80vh'}),
    html.Hr(),
    html.P("© 2026 Built with Python & Dash", className="text-center text-muted")
])

# Routing Callback
@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/dashboard': return dashboard.layout
    elif pathname == '/insights': return insights.layout
    elif pathname == '/about': return about.layout
    else: return home.layout

if __name__ == '__main__':
    app.run(debug=True)  # مسحنا كلمة _server
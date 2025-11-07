import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    html.H1("Personal financial dashboard"),
    className="p-5",
)

if __name__ == "__main__":
    app.run()
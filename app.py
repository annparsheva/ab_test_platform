from layout import Layout
from sample_size_utils import sample_size_calculate
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, ctx


app = Dash(__name__, external_stylesheets=[dbc.themes.LITERA])

server = app.server

app.layout = Layout().create_layout()


@app.callback(
    Output("sample-size", "children"),
    Input("significance-level-slider", "value"),
    Input("statistical-power-slider", "value"),
    Input("mde-input", "value"),
    Input("sd-input", "value"),
)
def display_value(significance_level, statistical_power, mde, sd):
    sample_size = sample_size_calculate(significance_level, statistical_power, mde, sd)
    text = f"Sample size > {sample_size}"
    return text


if __name__ == "__main__":
    app.run_server(debug=True)

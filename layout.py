import numpy as np
from dash import dcc, html
import dash_bootstrap_components as dbc


class Layout:
    def create_slider(self, min, max, value, step, label, id):
        if type(step) is int:
            marks = {str(i): str(i) for i in np.arange(min, max, step)}
        else:
            marks = {f"{i:.2}": f"{i:.2}" for i in np.arange(min, max, step)}

        slider = html.Div(
            [
                html.H6(label),
                dcc.Slider(
                    min, max, step=None, value=value, marks=marks, id=f"{id}-slider"
                ),
            ],
            style={"width": "70%"},
        )

        return slider

    def create_input(self, label, id, value):
        input = html.Div(
            [
                html.H6(label),
                dbc.Input(type="number", id=f"{id}-input", value=value),
            ],
            style={"width": "30%"},
        )
        return input

    def create_sample_size_block(self):
        significance_level_slider = self.create_slider(
            min=0,
            max=0.26,
            value=0.05,
            step=0.01,
            label="Significance level",
            id="significance-level",
        )
        statistical_power_slider = self.create_slider(
            min=60,
            max=100,
            value=80,
            step=5,
            label="Statistical power",
            id="statistical-power",
        )
        mde_input = self.create_input("MDE", "mde", 0.1)
        sd_input = self.create_input("SD (SDa = SDb)", "sd", 1)
        sample_size_block = html.Div(
            [
                html.H2("Sample size", className="mt-2"),
                html.Hr(),
                html.Div(
                    [significance_level_slider, mde_input],
                    style={"display": "flex", "justify-content": "space-between"},
                    className="mt-2",
                ),
                html.Div(
                    [statistical_power_slider, sd_input],
                    style={"display": "flex", "justify-content": "space-between"},
                    className="mt-2",
                ),
                dbc.Alert(
                    "",
                    color="info",
                    className="mt-2",
                    id="sample-size",
                    style={"width": "30%"},
                ),
            ]
        )

        return sample_size_block

    def create_layout(self):
        layout = dbc.Container([self.create_sample_size_block()])

        return layout

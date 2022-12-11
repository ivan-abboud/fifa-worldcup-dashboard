from dash import html
import dash_loading_spinners as dls
import utils.theme as theme
import dash_bootstrap_components as dbc
from app import app
from dash.dependencies import Output, Input, State
import pandas as pd
from app import tours as tours_df


def build_component(title="", src=""):
    return dbc.Col([html.Img(className="img-fluid m-2 rounded", src=src,
                             style={
                                 "box-shadow": "0 2px 6px 0 rgb(67 89 113 / 20%)"}
                             ),
                    html.Center(html.H6(title, className="m-0"))], className="col-lg-1 col-md-2 col-sm-4")


years = tours_df["year"].values
icons = [
    f"./assets/flags/4x3/{team}.svg" for team in tours_df["winner"].values]

winners = [build_component(y, icon) for y, icon in zip(years, icons)]


WCHeaderCard = html.Div(className="col-md-12 col-lg-12 mb-md-0 mb-4 card-chart-container", children=[
    html.Div(className="card", children=[
        html.Div(className="card-header card-m-0 me-2 pb-3", children=[
            html.H2("World Cup All Times Winners",
                    className="card-title text-center m-0 me-2", style={"font-size": "2vw"}),
        ]),

        dbc.Row(id="winners-first-row",
                className="mt-2 mb-2 p-3 justify-content-center", children=winners[:11]),
        dbc.Row(id="winners-second-row",
                className="mt-2 mb-2 p-3 justify-content-center", children=winners[11:])


    ], style={"align-text": "center"})
])

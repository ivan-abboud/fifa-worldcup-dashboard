import plotly.express as px
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from app import app

TeamRankingTable = html.Div(className="col-md-12 col-lg-4 mb-md-0 mb-4 card-chart-container", children=[
    html.Div(className="card", children=[
        html.Div(className="card-header card-m-0 me-2 pb-3", children=[
            html.H4("Standings in WorldCups", className="card-title m-0 me-2" , style={"font-size" : "1.5vw"}),
        ]),
        html.Div(className="table-responsive text-nowrap overflow-auto", children=[
            dls.Triangle(id="team-ranking-table",
                         children=[
                         ], debounce=theme.LOADING_DEBOUNCE)

        ], style={"height": theme.MAX_CHART_HEIGHT, "align-text": "center"})
    ])
])


@app.callback(
    Output("team-ranking-table", "children"),
    Input("query-team-select", "value"),
    State("qualified-teams-df" , "data")
)
def update_table(query_team, dataframe):
    dataframe = pd.read_json(dataframe)
    return dbc.Table.from_dataframe(dataframe.loc[dataframe.team_name == query_team], columns=["year", "performance", "count_matches"],
                                     header=["Year", "Standing",
                                             "Matches Count"],
                                     className=" no-footer", striped=False, bordered=False, hover=True)
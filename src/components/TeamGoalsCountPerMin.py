import plotly.express as px
import pandas as pd
from dash import html, dcc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from app import app
import numpy as np


TeamGoalsCountPerMin = html.Div(className="card-chart-container col-lg-8 md-6 sm-12",
                       children=[

                           html.Div(
                               className="card-chart",
                               children=[
                                   html.H4("Team Goals Count Per Minute",
                                           className="card-header card-m-0 me-2 pb-3"),
                                   dls.Triangle(
                                       id="team-goals-count-per-minute",
                                       children=[


                                       ], debounce=theme.LOADING_DEBOUNCE
                                   )
                               ]
                           )

                       ],
                       )


@app.callback(
    Output("team-goals-count-per-minute", "children"),
    Input("query-team-select", "value"),
    State("goals-df", "data")
)
def update_figures(query_team, goals_df):
    goals_df = pd.read_json(goals_df)
    tmp_df = pd.DataFrame({"minute":range(121),"count":np.zeros((121))})
    grouped_df = goals_df.loc[goals_df.team_name == query_team].groupby("minute_regulation", as_index=False).size()
    tmp_df = tmp_df.merge(grouped_df, how="left" , left_on="minute" , right_on="minute_regulation")
    tmp_df["goals_count"] = tmp_df["count"] + tmp_df["size"]
    tmp_df.fillna(0,inplace=True)
    return dcc.Graph(figure=px.line(tmp_df,
    x="minute", y="goals_count", labels={"goals_count":"Goals Count" , "minute": "Minute"} , color_discrete_sequence=theme.COLOR_PALLETE)
        .update_layout(paper_bgcolor="rgb(0,0,0,0)",
                       plot_bgcolor="rgb(0,0,0,0)",
                       legend=dict(
                           bgcolor=theme.LEGEN_BG),
                       font_family=theme.FONT_FAMILY,
                       ),
        config={
        "displayModeBar": False},
        style=theme.CHART_STYLE

    )

import plotly.express as px
import pandas as pd
from dash import html, dcc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from dash import callback

TeamGoalsStats = html.Div(className="card-chart-container col-lg-4 md-6 sm-12",
                          children=[
                              html.Div(
                                  className="card-chart",
                                  children=[
                                      html.H4("Scored vs. Conceded  Goals",
                                              className="card-header card-m-0 me-2 pb-3"),
                                      dls.Triangle(
                                          id="team-goals-stats",
                                          debounce=theme.LOADING_DEBOUNCE
                                      )
                                  ]
                              )

                          ],
                          )


@callback(
    Output("team-goals-stats", "children"),
    Input("query-team-select", "value"),
    State("team-stats-df", "data")
)
def update_team_goals_stats(query_team, team_stats_df):
    team_stats_df = pd.read_json(team_stats_df)
    team_stats_df = team_stats_df.loc[team_stats_df.team_name == query_team]
    goals_scored = team_stats_df["scored"].values[0]
    goals_conceded = team_stats_df["received"].values[0]

    return dcc.Graph(figure=px.bar(x=["Goals Scored", "Goals Conceded"], y=[goals_scored, goals_conceded], height=theme.MAX_CHART_HEIGHT,
                                   labels={"y": "Count", "x": ""}, color_discrete_sequence=theme.COLOR_PALLETE, text_auto=True,
                                   ).update_layout(paper_bgcolor="rgb(0,0,0,0)",
                                                   plot_bgcolor="rgb(0,0,0,0)",
                                                   legend=dict(
                                                       bgcolor=theme.LEGEN_BG),
                                                   font_family=theme.FONT_FAMILY,
                                                   ),
                     config={
        "displayModeBar": False},
        style=theme.CHART_STYLE

    )

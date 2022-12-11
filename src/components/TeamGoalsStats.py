import plotly.express as px
import pandas as pd
from dash import html, dcc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from app import app


TeamGoalsStats = html.Div(className="card-chart-container col-lg-4 md-6 sm-12",
                          children=[
                              html.Div(
                                  className="card-chart",
                                  children=[
                                      html.H4("Goals Scored vs. Goals Conceded",
                                              className="card-header card-m-0 me-2 pb-3"),
                                      dls.Triangle(
                                          id="team-goals-stats",
                                          debounce=theme.LOADING_DEBOUNCE
                                      )
                                  ]
                              )

                          ],
                          )


@app.callback(
    Output("team-goals-stats", "children"),
    Input("query-team-select", "value"),
    State("matches-df", "data")
)
def update_team_goals_stats(query_team, matches_df):
    matches_df = pd.read_json(matches_df)

    goals_scored = matches_df.loc[matches_df.home_team_name == query_team].home_team_score.sum(
    )+matches_df.loc[matches_df.away_team_name == query_team].away_team_score.sum()
    goals_recieved = matches_df.loc[matches_df.home_team_name == query_team].away_team_score.sum(
    ) + matches_df.loc[matches_df.away_team_name == query_team].home_team_score.sum()

    return dcc.Graph(figure=px.bar(x=["Goals Scored", "Goals Conceded"], y=[goals_scored, goals_recieved], height=theme.MAX_CHART_HEIGHT,
    labels={"y":"Count" , "x":""}, color_discrete_sequence=theme.COLOR_PALLETE, text=[goals_scored, goals_recieved],
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

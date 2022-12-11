import plotly.express as px
import pandas as pd
from dash import html, dcc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from app import app


TeamMatchesResults = html.Div(className="card-chart-container col-lg-4 md-6 sm-12",
                              children=[

                                  html.Div(
                                      className="card-chart",
                                      children=[
                                          html.H4("Overall Team Results",
                                                  className="card-header card-m-0 me-2 pb-3"),
                                          dls.Triangle(
                                              id="team-matches-results",
                                              children=[

                                              ], debounce=theme.LOADING_DEBOUNCE
                                          )
                                      ]
                                  )

                              ],
                              )


@app.callback(
    Output("team-matches-results", "children"),
    Input("query-team-select", "value"),
    State("matches-df", "data")
)
def update_team_matches_result(query_team, matches_df):
    matches_df = pd.read_json(matches_df)
    matches_df = matches_df.loc[(matches_df.home_team_name == query_team) | (
        matches_df.away_team_name == query_team)]

    win_as_home = matches_df.loc[(
        matches_df.home_team_name == query_team)].home_team_win.sum()
    lose_as_home = matches_df.loc[(
        matches_df.home_team_name == query_team)].away_team_win.sum()
    win_as_away = matches_df.loc[(
        matches_df.away_team_name == query_team)].away_team_win.sum()
    lose_as_away = matches_df.loc[(
        matches_df.away_team_name == query_team)].home_team_win.sum()
    draw = matches_df.draw.sum()

    return dcc.Graph(figure=px.pie(names=["Won", "Lost", "Draw"], values=[win_as_home+win_as_away, lose_as_home+lose_as_away, draw], hole=0.6,
                                    color_discrete_sequence=theme.COLOR_PALLETE,
                                   ).add_annotation(x=0.5, y=0.5,
                                               text=f'In {len(matches_df)} Matches',
                                               showarrow=False)
                                               .update_layout(paper_bgcolor="rgb(0,0,0,0)",
                                                   plot_bgcolor="rgb(0,0,0,0)",
                                                   legend=dict(
                                                       bgcolor=theme.LEGEN_BG),
                                                   font_family=theme.FONT_FAMILY,
                                                    margin={"t":40,"b":40,"l":32}
                                                   ),
                     config={
        "displayModeBar": False},
        style=theme.CHART_STYLE

    )

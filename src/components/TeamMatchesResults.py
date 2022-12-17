import plotly.express as px
import pandas as pd
from dash import html, dcc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from dash import callback

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


@callback(
    Output("team-matches-results", "children"),
    Input("query-team-select", "value"),
    State("team-stats-df", "data")
)
def update_team_matches_result(query_team, team_stats_df):

    team_stats_df = pd.read_json(team_stats_df)
    team_stats_df = team_stats_df.loc[team_stats_df.team_name == query_team]
    win_counts = team_stats_df["win_counts"].values[0]
    lose_counts = team_stats_df["lose_counts"].values[0]
    draw_counts = team_stats_df["draws"].values[0]
    matches_count = team_stats_df["count_matches"].values[0]

    return dcc.Graph(figure=px.pie(names=["Won", "Lost", "Draw"], values=[win_counts, lose_counts, draw_counts], hole=0.6,
                                   color_discrete_sequence=theme.COLOR_PALLETE,
                                   ).add_annotation(x=0.5, y=0.5,
                                                    text=f'In {matches_count} Matches',
                                                    showarrow=False)
                     .update_layout(paper_bgcolor="rgb(0,0,0,0)",
                                    plot_bgcolor="rgb(0,0,0,0)",
                                    legend=dict(
                                        bgcolor=theme.LEGEN_BG),
                                    font_family=theme.FONT_FAMILY,
                                    margin={"t": 40, "b": 40, "l": 32}
                                    ),
                     config={
        "displayModeBar": False},
        style=theme.CHART_STYLE

    )

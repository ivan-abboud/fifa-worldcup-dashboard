import plotly.express as px
import pandas as pd
from dash import html, dcc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from app import app


TeamResultsWithRival = html.Div(className="card-chart-container col-lg-4 md-6 sm-12",
                                children=[
                                    html.Div(
                                        className="card-chart",
                                        children=[
                                            html.H4("Matches Results",
                                                    className="card-header card-m-0 me-2 pb-3"),
                                            dls.Triangle(
                                                id="team-results-with-rival",
                                                debounce=theme.LOADING_DEBOUNCE
                                            )
                                        ]
                                    )
                                ],
                                )


@app.callback(
    Output("team-results-with-rival", "children"),
    Input("query-team-select", "value"),
    Input("rival-team-select", "value"),
    State("matches-df", "data")
)
def update_team_results_with_rival(query_team, rival, matches_df):
    matches_df = pd.read_json(matches_df)

    away_matches = matches_df.loc[(matches_df.away_team_name == query_team) & (
        matches_df.home_team_name == rival)]
    home_matches = matches_df.loc[(matches_df.home_team_name == query_team) & (
        matches_df.away_team_name == rival)]

    query_team_winning_times = away_matches.away_team_win.sum() + \
        home_matches.home_team_win.sum()
    rival_winning_times = away_matches.home_team_win.sum() + \
        home_matches.away_team_win.sum()
    draw_times = home_matches.draw.sum() + away_matches.draw.sum()


    return dcc.Graph(figure=px.pie(names=[f"{query_team} Won", f"{rival} Won", "Draw"], values=[query_team_winning_times, rival_winning_times, draw_times], hole=0.6,
                              color_discrete_sequence=theme.COLOR_PALLETE, height=386
                              ).add_annotation(x=0.5, y=0.5,
                                               text=f'{len(home_matches) + len(away_matches)} Matches',
                                               showarrow=False).update_layout(paper_bgcolor="rgb(0,0,0,0)",
                                                   plot_bgcolor="rgb(0,0,0,0)",
                                                   legend=dict(
                                                       bgcolor=theme.LEGEN_BG),
                                                   font_family=theme.FONT_FAMILY,
                                                   ),
                     config={
        "displayModeBar": False},

    )

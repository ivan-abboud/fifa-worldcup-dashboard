import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
import numpy as np
from dash import callback


RivalSectionTitle = html.Div([
    html.H2([html.Span("See How "), html.Span(id="rival-section-title",
            style={"color": theme.COLOR_PALLETE[0], }), html.Span(" Performed against other teams in WorldCup ")])
], style={"margin-top": "3rem"})


MatchesCount = html.Div(className="card mt-4" , children=[
                        html.Div(className="card-body", children=[
                            html.Div(className="d-flex justify-content-between", children=[

                                html.Div(className="card-info w-100",
                                         children=[html.Small(className="card-text", children=["Total Matches"]),
                                         html.Div(className="mb-2 mt-2", children=[
                                            dls.Triangle(
                                                   html.H2(className="card-title mb-2", id="matches-with-rival-count", style={"font-size":"2vw"}))]),
                                                   html.Small(
                                                       className="card-text", children=["Matches"], ),
                                                   
                                                   ], style={"text-align": "center"}),

                                html.Div(className="card-icon d-flex align-items-center w-50", children=[
                                    html.Img(className="img-fluid bx-lg",
                                             src="./assets/images/ic_soccer_ball.png", style={"width": "5rem",
                                                              })
                                ]
                                )
                            ])

                        ])
                    ])

TeamVsRivalMainCard = html.Div(className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container",
                               children=[html.Div(className="card", children=[
                                   html.Div(className="card-body", children=[
                                       html.Small("Choose Rival Team to see history with",
                                              className="card-text mt-1 mb-2",
                                              ),
                                       dbc.Select(id="rival-team-select"),
                                       html.Div(className="d-flex justify-content-between mt-3", children=[
                                           html.Div(className="card-info w-100",
                                                    children=[html.P(className="card-text mb-1 mt-1", id="rival-main-card-header"),
                                                              html.P(className="card-title mb-1 mt-1",
                                                                      id="rival-main-card-body",
                                                                      style={"font-size": "1rem"}),
                                                              html.A(children=[html.Small(id="rival-link-text")],id="rival-main-card-link",target="_blank")
                                                    ],
                                                    ),

                                           html.Div(className="card-icon d-flex align-items-center", children=[
                                               html.Img(className="img-fluid", id="rival-main-card-icon",alt="flag",
                                                        src="icon",style={"width" : "5em","box-shadow": "0 2px 6px 0 rgb(67 89 113 / 20%)"})
                                           ]
                                           )
                                       ]),
                                       html.P(
                                           className="card-text  mt-2", id="rival-main-card-subtitle", style={"font-size": "0.8em"})

                                   ])
                               ], style={"min-height": "17.2rem"}),
                               MatchesCount

                               ]
                               )


@callback(
    Output("rival-team-select", "options"),
    Output("rival-team-select", "value"),
    Output("rival-main-card-subtitle", "children"),
    Output("rival-section-title" , "children"),
    Input("query-team-select", "value"),
    State("matches-df", "data"),
)
def update_rival_select_options(query_team, matches_df):
    matches_df = pd.read_json(matches_df)

    away_teams = matches_df.loc[(
        matches_df.away_team_name == query_team)].home_team_name.unique()
    home_teams = matches_df.loc[(
        matches_df.home_team_name == query_team)].away_team_name.unique()
    rival_teams = set(away_teams)
    rival_teams = list(rival_teams.union(home_teams))
    rival_teams.sort()

    options = [{"label": l, "value": l} for l in rival_teams]
    card_subtitle = f"*Note: only teams that have played against {query_team} are shown in the list"

    

    return options, rival_teams[np.random.randint(0,len(rival_teams))], card_subtitle, query_team


@callback(
    Output("rival-main-card-icon", "src"),
    Output("rival-main-card-header" , "children"),
    Output("rival-main-card-body" , "children"),
    Output("rival-link-text" , "children"),
    Output("rival-main-card-link" , "href"),
    Input("rival-team-select", "value"),
    State("teams-df", "data")
)
def update_team_vs_rival_main_card(rival_team, teams_df):
    teams_df = pd.read_json(teams_df)

    team_code = f"Team Code: {teams_df.loc[teams_df.team_name==rival_team , 'team_code'].values[0]}"
    team_region = f"Region: {teams_df.loc[teams_df.team_name==rival_team , 'region_name'].values[0]}"
    wiki_link = teams_df.loc[teams_df.team_name==rival_team , 'team_wikipedia_link'].values[0]
    text_link = f"Read More About {rival_team}"


    icon = f"./assets/flags/4x3/{rival_team}.svg"
    return icon, team_code, team_region, text_link,wiki_link

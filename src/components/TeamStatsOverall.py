from components.StatsCardWithIcon import CardWithIcon
from dash.dependencies import Input, Output, State
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html
import dash_loading_spinners as dls
import utils.theme as theme
import os
from dash import callback
from utils.consts import *


wc_winning_times_card = html.Div(html.Div(className="card", children=[
    html.Div(className="card-body", children=[
        html.Div(className="d-flex justify-content-between", children=[
            html.Div(className="card-info w-100",
                     children=[
                         dls.Triangle(
                               html.H2(className="mb-2 mt-2 card-title mb-2",
                                       id="winning-times-text",
                                       style={"font-size": "4.2vw"})
                         ),
                         html.H6(
                             className="card-text m-0", children=["Times Winner"], style={"font-size": "1vw"}
                         ),
                         html.Small(
                             className="card-text", id="winning-years-text"
                         )
                     ], style={"text-align": "center"}),

            html.Div(className="card-icon d-flex align-items-center", children=[
                html.Img(className="img-fluid bx-lg",
                         src="./assets/images/ic_world_cup.png", style={"width": "8rem"})
            ]
            )
        ])

    ])
], style={"min-height": "12rem"}),
    className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container"
)

participations_card = html.Div(html.Div(className="card", children=[
    html.Div(className="card-body", children=[
        html.Div(className="d-flex justify-content-between", children=[
            html.Div(className="card-info w-100",
                     children=[
                         dls.Triangle(
                               html.H2(className="mb-2 mt-2 card-title mb-2",
                                       id="participation-text",
                                       style={"font-size": "4.2vw"})
                         ),
                         html.H6(
                             className="card-text m-0", children=["Participations"], style={"font-size": "1vw"}
                         ),
                     ], style={"text-align": "center"}),

            html.Div(className="card-icon d-flex align-items-center", children=[
                html.Img(className="img-fluid bx-lg",
                         src="./assets/images/ic_stadium.png", style={"width": "8rem"})
            ]
            )
        ])

    ])
], style={"min-height": "12rem"}),
    className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container"
)


matches_count_card = html.Div(html.Div(className="card", children=[
    html.Div(className="card-body", children=[
        html.Div(className="d-flex justify-content-between", children=[
            html.Div(className="card-info w-100",
                     children=[
                         dls.Triangle(
                               html.H2(className="mb-2 mt-2 card-title mb-2",
                                       id="matches-count-text",
                                       style={"font-size": "4.2vw"})
                         ),
                         html.H6(
                             className="card-text m-0", children=["Matches"], style={"font-size": "1vw"}
                         ),
                     ], style={"text-align": "center"}),

            html.Div(className="card-icon d-flex align-items-center", children=[
                html.Img(className="img-fluid bx-lg",
                         src="./assets/images/ic_soccer_ball.png", style={"width": "9rem"})
            ]
            )
        ])

    ])
], style={"min-height": "12rem"}),
    className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container"
)


TeamStatsOverall = dbc.Row(children=[
    html.Div(className="col-lg-3 col-md-6 col-sm-12 card-chart-container", children=[html.Div(className="card", children=[
        html.Div(className="card-body", children=[
            html.Div(className="d-flex justify-content-between", children=[
                html.Div(className="card-info",
                         children=[
                             dbc.Select(
                                 id="query-team-select",
                                 value="Brazil",
                                 options=[
                                     {"label": l, "value": l} for l in teams.team_name.values if l != "Israel"
                                 ],
                                 style={"width": "10rem"}
                             ),
                             html.P(className="card-text mb-1 mt-1",
                                    id="team-code-text",
                                    children=[f"Team Code: "]),
                             html.P(className="card-text mb-1",
                                    id="team-region-text",
                                    children=[f"Region:"]),
                             html.P(className="card-text mb-1",
                                    id="team-confederation-text",
                                    children=[f"Conf: "]),
                             html.A(id="query-team-wiki-link",
                                    target="_blank",
                                    style={"font-size": "0.9rem"})
                         ]),
                html.Div(className="card-icon d-flex align-items-center w-40 justify-content-center", children=[
                    dls.Triangle(
                        html.Img(className="img-fluid bx-lg",
                                 id="team-flag-main",
                                 style={
                                     "width": "2em", "box-shadow": "0 2px 6px 0 rgb(67 89 113 / 20%)"}
                                 ),
                        debounce=theme.LOADING_DEBOUNCE
                    )
                ]
                )

            ])

        ])
    ], style={"min-height": "12rem"})]
    ),
    wc_winning_times_card,

    participations_card,

    matches_count_card,
])


# @callback(
#     Output("winning-times-text", "children"),
#     Output("winning-years-text", "children"),
#     Output("participation-text","children"),
#     Output("matches-count-text" , "children"),
#     Input("query-team-select", "value"),
# )
# def update_team_stats(query_team):

#     matches_count = team_stats.loc[team_stats.team_name ==
#                                    query_team]["count_matches"].values[0]
#     winning_times = team_stats.loc[team_stats.team_name ==
#                                    query_team]["winning_times"].values[0]
#     participation_count = team_stats.loc[team_stats.team_name ==
#                                          query_team]["participations"].values[0]

#     winning_years = "- ".join(tours.loc[tours.winner ==
#                                         query_team, "year"].values.astype("str"))

#     return winning_times, winning_years, participation_count, matches_count


@callback(
    Output("team-code-text", "children"),
    Output("team-region-text", "children"),
    Output("team-confederation-text", "children"),
    Output("team-flag-main", "src"),
    Output("query-team-wiki-link", "href"),
    Output("query-team-wiki-link", "children"),

    Output("winning-times-text", "children"),
    Output("winning-years-text", "children"),
    Output("participation-text", "children"),
    Output("matches-count-text", "children"),

    Input("query-team-select", "value"),
    State("teams-df", "data"),
)
def update_team_select(query_team, teams_df):
    teams_df = pd.read_json(teams_df)
    team_code = f"Team Code: {teams_df.loc[teams_df.team_name==query_team , 'team_code'].values[0]}"
    team_region = f"Region: {teams_df.loc[teams_df.team_name==query_team , 'region_name'].values[0]}"
    team_confederation = f"Confedration: {teams_df.loc[teams_df.team_name==query_team , 'confederation_code'].values[0]}"
    team_flag = f"./assets/flags/4x3/{query_team}.svg"
    wiki_link = teams_df.loc[teams_df.team_name ==
                             query_team, 'team_wikipedia_link'].values[0]

    matches_count = team_stats.loc[team_stats.team_name ==
                                   query_team]["count_matches"].values[0]
    winning_times = team_stats.loc[team_stats.team_name ==
                                   query_team]["winning_times"].values[0]
    participation_count = team_stats.loc[team_stats.team_name ==
                                         query_team]["participations"].values[0]

    winning_years = "- ".join(tours.loc[tours.winner ==
                                        query_team, "year"].values.astype("str"))

    return team_code, team_region, team_confederation, team_flag, wiki_link, f"Read More About {query_team}", winning_times, winning_years, participation_count, matches_count

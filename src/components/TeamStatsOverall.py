from components.StatsCardWithIcon import CardWithIcon
from dash.dependencies import Input, Output, State
from app import app
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html
import dash_loading_spinners as dls
import utils.theme as theme
from app import DATA_FOLDER, ASSETS_FOLDER
import os

teams = pd.read_csv(os.path.join(DATA_FOLDER +"processed/teams.csv"))


def StatsCard(icon, card_header="", card_body="", card_tail="", class_name="", card_subtitle=" ", icon_width="9rem", icon_class_name="img-fluid bx-lg"):
    return html.Div(className="card", children=[
                        html.Div(className="card-body", children=[
                            html.Div(className="d-flex justify-content-between", children=[

                                html.Div(className="card-info w-100",
                                         children=[html.Small(className="card-text", children=[card_header]),

                                                   html.H2(className="mb-2 mt-2 card-title mb-2",
                                                           children=[
                                                               card_body],
                                                           style={"font-size": "4.2vw"}),


                                                   html.H6(
                                             className="card-text m-0", children=[card_tail], style={"font-size": "1vw"}
                                         ),
                                             html.Small(
                                             className="card-text", children=[card_subtitle]
                                         )
                                         ], style={"text-align": "center"}),

                                html.Div(className="card-icon d-flex align-items-center", children=[
                                    html.Img(className=icon_class_name,
                                             src=icon, style={"width": icon_width,
                                                              })
                                ]
                                )
                            ])

                        ])
                    ], style={"min-height": "12rem"})
                    


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
    html.Div(className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container",id="team-stats-wc-winning"),

    html.Div(className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container",id="team-stats-participation"),

    html.Div(className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container",id="team-stats-matches"),
])


@app.callback(
    Output("team-stats-wc-winning", "children"),
    Output("team-stats-participation", "children"),
    Output("team-stats-matches", "children"),
    Input("query-team-select", "value"),
    State("matches-df", "data"),
    State("qualified-teams-df", "data"),
    State("tours-df", "data"),
)
def update_team_stats(query_team, matches_df, qualified_teams_df, tours_df):
    matches_df = pd.read_json(matches_df)
    tours_df = pd.read_json(tours_df)
    qualified_teams_df = pd.read_json(qualified_teams_df)

    matches_count = len(matches_df.loc[(matches_df.home_team_name == query_team) | (
        matches_df.away_team_name == query_team)])
    winning_times = len(tours_df.loc[tours_df.winner == query_team])
    winning_years = "- ".join(tours_df.loc[tours_df.winner ==
                                           query_team, "year"].values.astype("str"))
    participation_count = len(
        qualified_teams_df.loc[qualified_teams_df.team_name == query_team])

    winning_times_card = StatsCard(icon=os.path.join(ASSETS_FOLDER,"/images/ic_world_cup.png"),  card_body=f"{winning_times}",
                                   card_subtitle=winning_years, card_tail="Times Winner", icon_width="8rem")

    participation_count_card = StatsCard(icon=os.path.join(ASSETS_FOLDER,"images/ic_stadium.png"),  card_body=f"{participation_count}",
                                         card_tail="Participations")

    matches_count_card = StatsCard(icon=os.path.join(ASSETS_FOLDER,"images/ic_soccer_ball.png"),
                                   card_body=f"{matches_count}", card_tail="Matches", icon_width="9rem", icon_class_name="img-fluid")

    return winning_times_card, participation_count_card, matches_count_card


@app.callback(
    Output("team-code-text", "children"),
    Output("team-region-text", "children"),
    Output("team-confederation-text", "children"),
    Output("team-flag-main", "src"),
    Output("query-team-wiki-link", "href"),
    Output("query-team-wiki-link", "children"),
    Input("query-team-select", "value"),
    State("teams-df", "data"),
)
def update_team_select(query_team, teams_df):
    teams_df = pd.read_json(teams_df)
    team_code = f"Team Code: {teams_df.loc[teams_df.team_name==query_team , 'team_code'].values[0]}"
    team_region = f"Region: {teams_df.loc[teams_df.team_name==query_team , 'region_name'].values[0]}"
    team_confederation = f"Confedration: {teams_df.loc[teams_df.team_name==query_team , 'confederation_code'].values[0]}"
    team_flag = os.path.join(ASSETS_FOLDER, f"/flags/4x3/{query_team}.svg")
    wiki_link = teams_df.loc[teams_df.team_name ==
                             query_team, 'team_wikipedia_link'].values[0]
    return team_code, team_region, team_confederation, team_flag, wiki_link, f"Read More About {query_team}"

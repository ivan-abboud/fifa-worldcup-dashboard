from dash.dependencies import Input, Output, State
import pandas as pd
from dash import html, callback

yellow_cards = html.Div(className="col-md-12 col-lg-12 mb-md-0 mb-4",
                        children=[html.Div(className="card", children=[
                            html.Div(className="card-body", children=[
                                html.Div(className="d-flex justify-content-between", children=[

                                    html.Div(className="card-info w-100",
                                         children=[html.Small(className="card-text", children=["Yellow Cards"]),
                                                   html.H2(className="mb-2 mt-2 card-title mb-2",
                                                   id="yellow-card-body",


                                                           #    children=[
                                                           #        card_body],
                                                           style={"font-size": "4vw"}),
                                                   #    html.H6(
                                                   #        className="card-text m-0", children=[card_tail], style={"font-size": "1rem"}),
                                                   html.Small(className="card-text",
                                                              id="yellow-card-subtitle"
                                                              )
                                                   ], style={"text-align": "center"}),

                                    html.Div(className="card-icon d-flex align-items-center w-50", children=[
                                        html.Img(className="img-fluid bx-lg",
                                             src="./assets/images/yellow-card.png", style={"width": "6rem",
                                                                                           })
                                    ]
                                    )
                                ])

                            ])
                        ])
                        ]
                        )


red_cards = html.Div(className="col-md-12 col-lg-12 mb-md-0 mb-4",
                        children=[html.Div(className="card", children=[
                            html.Div(className="card-body", children=[
                                html.Div(className="d-flex justify-content-between", children=[

                                    html.Div(className="card-info w-100",
                                         children=[html.Small(className="card-text", children=["Red Cards"]),
                                                   html.H2(className="mb-2 mt-2 card-title mb-2",
                                                   id="red-card-body",


                                                           #    children=[
                                                           #        card_body],
                                                           style={"font-size": "4vw"}),
                                                   #    html.H6(
                                                   #        className="card-text m-0", children=[card_tail], style={"font-size": "1rem"}),
                                                   html.Small(className="card-text",
                                                              id="red-card-subtitle"
                                                              )
                                                   ], style={"text-align": "center"}),

                                    html.Div(className="card-icon d-flex align-items-center w-50", children=[
                                        html.Img(className="img-fluid bx-lg",
                                             src="./assets/images/red-card.png", style={"width": "6rem",
                                                                                           })
                                    ]
                                    )
                                ])

                            ])
                        ])
                        ]
                        )

TeamBookings = html.Div(
    className="col-md-12 col-lg-2 mb-md-0 mb-4 card-chart-container d-flex flex-column justify-content-between", id="team-bookings",
    children=[
        yellow_cards,
        red_cards
    ]
)


@callback(
    Output("yellow-card-body", "children"),
    Output("yellow-card-subtitle", "children"),
    Output("red-card-body", "children"),
    Output("red-card-subtitle", "children"),
    Input("query-team-select", "value"),
    State("team-stats-df", "data"),
)
def update_team_bookings(query_team, team_stats_df):
    team_stats_df = pd.read_json(team_stats_df)
    yellow_card_counts = team_stats_df.loc[team_stats_df.team_name == query_team]["yellow_cards"].values[0]
    red_card_counts = team_stats_df.loc[team_stats_df.team_name == query_team]["red_cards"].values[0]
    matches_count = team_stats_df.loc[team_stats_df.team_name == query_team]["count_matches"].values[0]

    
    matches_count_text = f"In {matches_count} Matches"
    return yellow_card_counts,matches_count_text,red_card_counts,matches_count_text

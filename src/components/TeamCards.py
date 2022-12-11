from components.StatsCardWithIcon import CardWithIcon
from dash.dependencies import Input, Output, State
import pandas as pd
from dash import html, callback


def StatsCard(icon, card_header="", card_body="", card_tail="", class_name="", card_subtitle=""):
    return html.Div(className="col-md-12 col-lg-12 mb-md-0 mb-4" + class_name,
                    children=[html.Div(className="card", children=[
                        html.Div(className="card-body", children=[
                            html.Div(className="d-flex justify-content-between", children=[

                                html.Div(className="card-info w-100",
                                         children=[html.Small(className="card-text", children=[card_header]),
                                                   html.H2(className="mb-2 mt-2 card-title mb-2",
                                                           children=[
                                                               card_body],
                                                           style={"font-size": "4vw"}),
                                                   html.H6(
                                                       className="card-text m-0", children=[card_tail], style={"font-size": "1rem"}),
                                                   html.Small(className="card-text", children=[card_subtitle]
                                                              )
                                                   ], style={"text-align": "center"}),

                                html.Div(className="card-icon d-flex align-items-center w-50", children=[
                                    html.Img(className="img-fluid bx-lg",
                                             src=icon, style={"width": "6rem",
                                                              })
                                ]
                                )
                            ])

                        ])
                    ])
                    ]
                    )


TeamBookings = html.Div(
    className="col-md-12 col-lg-2 mb-md-0 mb-4 card-chart-container d-flex flex-column justify-content-between", id="team-bookings")


@callback(
    Output("team-bookings", "children"),
    Input("query-team-select", "value"),
    State("bookings-df", "data"),
    State("matches-df", "data"),
)
def update_team_bookings(query_team, bookings_df, matches_df):
    matches_df = pd.read_json(matches_df)
    bookings_df = pd.read_json(bookings_df)
    yellow_cards_count = len(bookings_df.loc[(
        bookings_df.team_name == query_team) & (bookings_df.yellow_card)])
    red_cards_count = len(
        bookings_df.loc[(bookings_df.team_name == query_team) & (bookings_df.red_card)])
    matches_count = len(matches_df.loc[(matches_df.home_team_name == query_team) | (matches_df.away_team_name == query_team)])

    yellow_cards = StatsCard(icon="./assets/images/yellow-card.png", card_header="Yellow Cards",
                             card_body=f"{yellow_cards_count}", card_subtitle=f"In {matches_count} Matches")
    red_cards = StatsCard(icon="./assets/images/red-card.png", card_header="Red Cards",
                          card_body=f"{red_cards_count}", card_subtitle=f"In {matches_count} Matches" , class_name="")
    return [yellow_cards, red_cards]

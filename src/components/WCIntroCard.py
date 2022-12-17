from dash import html
import dash_bootstrap_components as dbc
from utils.consts import LINKEDIN_PROFILE

WCIntroCard = html.Div(className="col-md-12 col-lg-12 mb-md-0 mb-4 card-chart-container", children=[

    html.Div(className="card", children=[
        dbc.Row([
            dbc.Col(className="col-lg-6", children=[html.Div(className="card-header card-m-0 me-2 pb-3", children=[
                html.H2(["FIFA World Cup Dashboard"],
                    className="card-title m-0 me-2 mb-2", style={"font-size": "2vw"}),
                html.Span(
                    "From Data Science Point-of-View", style={"color": "#0084d6", "font-size": "1.5vw"})
            ]),
                html.P(["This dashboard presents all you need to know about FIFA World Cup tournaments through history: winners, hosting countries, matches, and more. You can also check each team's statistics and compare teams with each other in the",
                        html.A(" Teams tab.", href="/team-analysis",
                               style={"color": "#0084d6"}),
                        html.P(
                            "*Note: dashboard doesn't include Qatar 2022 WorldCup data.", className="mt-1")
                        ], className="card-title me-4"),


                html.P(["Please feel free to report any problems or reach me directely,",
                        html.A(" Ivan Abboud.", href=LINKEDIN_PROFILE, target="_blank", style={"color": "#0084d6"})], className="card-title me-4 mb-0 mt-4"),

            ]),

            dbc.Col(className="col-lg-6", children=[html.Img(
                src="./assets/images/players_background.png", className="img-fluid")], style={"align-self": "self-end"})
        ]),

    ])
])

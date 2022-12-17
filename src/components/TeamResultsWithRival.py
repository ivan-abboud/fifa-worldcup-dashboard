from dash import html
import utils.theme as theme
import pandas as pd
import dash_loading_spinners as dls

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

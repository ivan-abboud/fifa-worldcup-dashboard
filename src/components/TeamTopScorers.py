import plotly.express as px
import pandas as pd
from dash import html, dcc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from app import app


TeamTopScorers = html.Div(className="card-chart-container col-lg-4 md-6 sm-12",
                                  children=[

                                      html.Div(
                                          className="card-chart",
                                          children=[
                                              html.H4("Team Top Scorers",
                                                      className="card-header card-m-0 me-2 pb-3"),
                                              dls.Triangle(
                                                  id="team-top-scorers",
                                                  children=[


                                                  ], debounce=theme.LOADING_DEBOUNCE
                                              )
                                          ]
                                      )

                                  ],
                                  )


@app.callback(
    Output("team-top-scorers", "children"),
    Input("query-team-select", "value"),
    State("goals-df", "data")
)
def update_figures(query_team, goals_df):
    goals_df = pd.read_json(goals_df)
    return dcc.Graph(figure=px.bar(goals_df.loc[goals_df.team_name == query_team].groupby("family_name", as_index=False).size().sort_values(by="size", ascending=False).head(10),
    x="family_name", y="size" , labels={"size":"Goals Count" , "family_name":"Player"} , color_discrete_sequence=theme.COLOR_PALLETE)
                     .update_layout(paper_bgcolor="rgb(0,0,0,0)",
                                    plot_bgcolor="rgb(0,0,0,0)",
                                    legend=dict(
                                        bgcolor=theme.LEGEN_BG),
                                    font_family=theme.FONT_FAMILY,
                                    ),
                     config={
        "displayModeBar": False},
        style=theme.CHART_STYLE

    )

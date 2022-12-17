import plotly.express as px
import pandas as pd
from dash import html, dcc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from dash import callback

TeamGoalsCountPerShirt = html.Div(className="card-chart-container col-lg-4 md-6 sm-12",
                                  children=[

                                      html.Div(
                                          className="card-chart",
                                          children=[
                                              html.H4("Goals Count Per Shirt Number",
                                                      className="card-header card-m-0 me-2 pb-3"),
                                              dls.Triangle(
                                                  id="team-goals-count-per-shirt-num",
                                                  children=[


                                                  ], debounce=theme.LOADING_DEBOUNCE
                                              )
                                          ]
                                      )

                                  ],
                                  )


@callback(
    Output("team-goals-count-per-shirt-num", "children"),
    Input("query-team-select", "value"),
    State("goals-df", "data")
)
def update_figures(query_team, goals_df):
    goals_df = pd.read_json(goals_df)
    return dcc.Graph(figure=px.bar(goals_df.loc[(goals_df.team_name == query_team) & (goals_df.shirt_number != 0)].groupby("shirt_number", as_index=False).size(),
                                   x="shirt_number", y="size", labels={"size": "Goals Count", "shirt_number": "Shirt Number"}, color_discrete_sequence=theme.COLOR_PALLETE)
                     .update_xaxes(type="category")
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

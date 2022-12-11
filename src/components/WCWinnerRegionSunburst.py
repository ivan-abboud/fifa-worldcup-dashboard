
import plotly.express as px
from app import tours, teams
from dash import html, dcc
import utils.theme as theme


sunburst_df = tours.groupby("winner",as_index=False).size().merge(teams[["team_name" , "region_name"]],how="left" , left_on="winner" , right_on="team_name")

WCWinnerRegion = html.Div(className="card-chart-container col-lg-4 col-md-12 col-sm-12", children=[
    html.Div(
        className="card-chart",
        children=[
            html.H4("World Cup Holders By Region",
                        className="card-header card-m-0 me-2 pb-3",style={"font-size": "1.5vw"}),
            dcc.Graph(
                    figure=px.sunburst(
                        sunburst_df,
                        path=["region_name" , "team_name"],
                        values="size",
                        height=theme.MAX_CHART_HEIGHT,
                        color_discrete_sequence=theme.COLOR_PALLETE,
                    ).update_layout(
                        font_family=theme.FONT_FAMILY,
                        margin={"t":5,"l":0,"r":0,"b":30}
                    ),
                    config={"displayModeBar": False},
                    
                    )
        ],
    ),
])
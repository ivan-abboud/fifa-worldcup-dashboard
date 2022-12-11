import plotly.express as px
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc
import utils.theme as theme
import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_loading_spinners as dls
from app import app
from components.TeamRankingTable import TeamRankingTable
from components.TeamGoalsCountPerTour import TeamGoalsCountPerTour
from components.TeamGoalsCountPerMin import TeamGoalsCountPerMin
from components.TeamGoalsCountPerShirt import TeamGoalsCountPerShirt
from components.TeamTopScorers import TeamTopScorers
from components.TeamMatchesResults import TeamMatchesResults
from components.TeamGoalsStats import TeamGoalsStats
from components.TeamResultsWithRival import TeamResultsWithRival
from components.TeamGamesWithRivalTable import TeamGamesWithRivalTable
from components.TeamStatsOverall import TeamStatsOverall
from components.TeamCards import TeamBookings
from components.TeamVsRivalMainCard import TeamVsRivalMainCard, RivalSectionTitle


query_team = "Brazil"



team_analysis_page_content = html.Div(children=[
    TeamStatsOverall,
    dbc.Row(children=[
        TeamRankingTable,
        TeamGoalsCountPerTour,
        TeamBookings


    ]),
    dbc.Row(children=[
        TeamTopScorers,
        TeamMatchesResults,
        TeamGoalsStats

    ]),
    dbc.Row(children=[
        TeamGoalsCountPerMin,
        TeamGoalsCountPerShirt

    ]),
    dbc.Row(children=[
        RivalSectionTitle
    ]),
    dbc.Row(children=[
        TeamVsRivalMainCard,
        TeamGamesWithRivalTable,
        TeamResultsWithRival,

    ]),
], style={"padding-top": "3rem"})

from dash import html
import dash_bootstrap_components as dbc
from components.WC_Header import WCHeaderCard
from components.WCWinnerRegionSunburst import WCWinnerRegion
from components.WCComponents import *
from components.WCIntroCard import WCIntroCard


worldcup_page_content = html.Div([
    dbc.Row([
            WCIntroCard,
            ]),

    dbc.Row([
        WCHeaderCard
    ]),
    dbc.Row([
        WCWinnersBar,
        WCWinnerRegion,
        HostsCountriesBar,

    ]),
    dbc.Row([
        VenuesAndCitiesBar,
        TotalAttendanceLine,

    ]),
    dbc.Row([
        ToursTimeline,
        MatchesCountBar,
    ]),
    dbc.Row([
        MostAttendedMatchesBar,
        dbc.Col([GoalsCountPerTourLine,
                 GoalsCountPerMinute, ], className="m-0 p-0")
    ]),


    dbc.Row([
    ]),
    dbc.Row([
        dbc.Col([CountriesTotalGoalsBar,
                 CountriesAwardsBar], className="m-0 p-0"),

        TopWcScorersBar,
    ]),


    dbc.Row([

    ]),
], style={"padding-top": "40px"})

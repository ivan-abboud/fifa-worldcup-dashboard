import sys
import os
module_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__))))
if module_path not in sys.path:
    sys.path.append(module_path)

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
import pandas as pd
from components.NavbarVertical import sidebar
from components.Footer import Footer
from dash.dependencies import Input, Output
from pages.worldcup_analysis import worldcup_page_content
from pages.team_analysis import team_analysis_page_content
from pages.about import about_page_content
import glob
from utils.consts import team_stats
from components import TeamsComponentsCallbacks



# RAW

import os
ROOT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
SRC_FOLDER = os.path.join(ROOT_FOLDER, "src/")
DATA_FOLDER = os.path.join(ROOT_FOLDER, "data/")
ASSETS_FOLDER = os.path.join(SRC_FOLDER, "assets")

# Processed
teams = pd.read_csv(os.path.join(DATA_FOLDER, "processed/teams.csv"))
bookings = pd.read_csv(os.path.join(ROOT_FOLDER,"data/processed/bookings.csv"))
award_winners = pd.read_csv(os.path.join(ROOT_FOLDER,"data/processed/award_winners.csv"))
data = pd.read_csv(os.path.join(ROOT_FOLDER,"data/processed/qualified_teams.csv"))
goals = pd.read_csv(os.path.join(ROOT_FOLDER,"data/processed/goals.csv"))
tours = pd.read_csv(os.path.join(ROOT_FOLDER,"data/processed/tournaments.csv"))
matches = pd.read_csv(os.path.join(ROOT_FOLDER,"data/processed/matches.csv"))


data_store = html.Div([dcc.Store(id="qualified-teams-df", data=data.to_json()),
                       dcc.Store(id="goals-df", data=goals.to_json()),
                       dcc.Store(id="matches-df", data=matches.to_json()),
                       dcc.Store(id="tours-df", data=tours.to_json()),
                       dcc.Store(id="teams-df", data=teams.to_json()),
                       dcc.Store(id="bookings-df", data=bookings.to_json()),
                       dcc.Store(id="team-stats-df", data=team_stats.to_json())])

external_style_sheet = glob.glob(os.path.join(ASSETS_FOLDER,"bootstrap/css") + "/*.css")
external_style_sheet += glob.glob(os.path.join(ASSETS_FOLDER,"css") + "/*.css")
external_style_sheet += glob.glob(os.path.join(ASSETS_FOLDER,"fonts") + "/*.css")



app = dash.Dash(__name__,title="WorldCup Dashboard",
                external_stylesheets=[dbc.themes.BOOTSTRAP] + external_style_sheet,
                suppress_callback_exceptions=True
                )

server = app.server


app.layout = html.Div(className="layout-wrapper layout-content-navbar",
         children=[
             html.Div(className="layout-container",
                      children=[
                        dcc.Location(id="url"),
                      data_store,
                          html.Aside(className="",
                                     children=[
                                        sidebar

                                     ]),
                          html.Div(className="layout-page",
                                   children=[
                                       html.Div(className="content-wrapper",
                                                children=[
                                                    html.Div(className="container-xxl flex-grow-1 container-p-y p-0",
                                                                id="page-content",
                                                             children=[

                                                             ]),
                                                    html.Footer(className="content-footer footer bg-footer-theme",
                                                                children=[
                                                                    Footer
                                                                ],style={"margin-left":"6rem"})

                                                ])
                                   ])

                      ])
         ])

@callback(
    Output(component_id='page-content', component_property='children'),
    Input(component_id='url', component_property='pathname')
)
def routing(path):
    if path == "/":
        return worldcup_page_content
    elif path == "/team-analysis":
        return team_analysis_page_content
    elif path == "/about":
        return about_page_content


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=5050)
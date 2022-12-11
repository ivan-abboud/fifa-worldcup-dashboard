import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import pandas as pd

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
                       dcc.Store(id="bookings-df", data=bookings.to_json())])

app = dash.Dash(title="WorldCup Dashboard",
                external_stylesheets=[dbc.themes.BOOTSTRAP,
                                      os.path.join(ASSETS_FOLDER,"bootstrap/bootstrap.min.css")],
                suppress_callback_exceptions=True
                )

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import pandas as pd

# RAW
teams = pd.read_csv("./data/raw/teams.csv")
bookings = pd.read_csv("./data/raw/bookings.csv")
award_winners = pd.read_csv("./data/raw/award_winners.csv")

# Processed
data = pd.read_csv("./data/processed/qualified_teams.csv")
goals = pd.read_csv("./data/processed/goals.csv")
tours = pd.read_csv("./data/processed/tournaments.csv")
matches = pd.read_csv("./data/processed/matches.csv")


data_store = html.Div([dcc.Store(id="qualified-teams-df", data=data.to_json()),
                       dcc.Store(id="goals-df", data=goals.to_json()),
                       dcc.Store(id="matches-df", data=matches.to_json()),
                       dcc.Store(id="tours-df", data=tours.to_json()),
                       dcc.Store(id="teams-df", data=teams.to_json()),
                       dcc.Store(id="bookings-df", data=bookings.to_json())])

app = dash.Dash(title="WorldCup Dashboard",
                external_stylesheets=[dbc.themes.BOOTSTRAP,
                                      "./assets/bootstrap/bootstrap.min.css"],
                suppress_callback_exceptions=True
                )

server = app.server
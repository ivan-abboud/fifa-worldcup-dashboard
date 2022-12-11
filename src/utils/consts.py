import os
import pandas as pd
SRC_FOLDER = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
#SRC_FOLDER = os.path.join(ROOT_FOLDER)
DATA_FOLDER = os.path.join(os.path.dirname(os.path.abspath(SRC_FOLDER)), "data/")
ASSETS_FOLDER = os.path.join(os.path.dirname(os.path.abspath(SRC_FOLDER)), "src/assets/")

teams = pd.read_csv(os.path.join(DATA_FOLDER, "processed/teams.csv"))
bookings = pd.read_csv(os.path.join(DATA_FOLDER,"processed/bookings.csv"))
award_winners = pd.read_csv(os.path.join(DATA_FOLDER,"processed/award_winners.csv"))
data = pd.read_csv(os.path.join(DATA_FOLDER,"processed/qualified_teams.csv"))
goals = pd.read_csv(os.path.join(DATA_FOLDER,"processed/goals.csv"))
tours = pd.read_csv(os.path.join(DATA_FOLDER,"processed/tournaments.csv"))
matches = pd.read_csv(os.path.join(DATA_FOLDER,"processed/matches.csv"))
import pandas as pd
from dash import html
import utils.theme as theme
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from app import app
import dash_bootstrap_components as dbc
from components.StatsCardWithIcon import CardWithIcon



TeamGamesWithRivalTable = html.Div(className="col-md-6 col-lg-5 mb-md-0 mb-4 card-chart-container", children=[

    html.Div(className="card", children=[
        html.Div(className="card-header d-flex align-items-center justify-content-between", children=[
            html.H5(id="team-rival-history", className="card-title m-0 me-2"),
        ]),
        html.Div(className="table-responsive text-nowrap overflow-auto", children=[
            dls.Triangle(
                id="team-games-with-rival-table",
                debounce=theme.LOADING_DEBOUNCE
            )

        ], style={"height": "13rem"})
    ]),

    dbc.Row(className="row-lg-12 me-0 pt-4",
            id="competitors-goals-count"),


])


@app.callback(
    Output("team-games-with-rival-table", "children"),
    Output("competitors-goals-count", "children"),
    Output("team-rival-history" , "children"),
    Output("matches-with-rival-count" , "children"),
    Input("query-team-select", "value"),
    Input("rival-team-select", "value"),
    State("matches-df", "data")
)
def update_team_games_with_rival(query_team, rival, matches_df):
    matches_df = pd.read_json(matches_df)

    away_matches = matches_df.loc[(matches_df.away_team_name == query_team) & (
        matches_df.home_team_name == rival)]
    home_matches = matches_df.loc[(matches_df.home_team_name == query_team) & (
        matches_df.away_team_name == rival)]

    all_matches_df = pd.concat([home_matches[['year', 'stage_name', 'home_team_name', 'away_team_name', 'score', ]],
                                away_matches[['year', 'stage_name', 'home_team_name', 'away_team_name', 'score']]]).sort_values(by="year")

    table = dbc.Table.from_dataframe(all_matches_df,
                                     header=["Year", "Stage",
                                             "Home Team", "Away Team", "Score"],
                                     className="table no-footer", striped=False, bordered=False, hover=True)
    qt_goals_card = CardWithIcon(
        f"./assets/flags/4x3/{query_team}.svg"
        , f"{query_team} Scored",
        f"{away_matches.away_team_score.sum() + home_matches.home_team_score.sum()} Goals",
        f"in {len(all_matches_df)} Matches","ps-0 pe-2")
    rival_goals_card = CardWithIcon(
        f"./assets/flags/4x3/{rival}.svg",
        f"{rival} Scored", f"{away_matches.home_team_score.sum() + home_matches.away_team_score.sum()} Goals", f"in {len(all_matches_df)} Matches","ps-2 pe-0")
    return table, [qt_goals_card,rival_goals_card], f"{query_team} and {rival} History", len(all_matches_df)

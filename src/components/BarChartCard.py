import plotly.express as px
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc
import utils.theme as theme
from app import tours

# data = pd.read_csv("./data/processed/tournaments.csv")
# award_winners = pd.read_csv("./data/raw/award_winners.csv")
# award_winners.loc[award_winners.team_name ==
#                   "West Germany", "team_name"] = "Germany"

# goals = pd.read_csv("./data/raw/goals.csv")
# goals.loc[goals.team_name == "West Germany", "team_name"] = "Germany"

# CARD_HEIGHT = 400


# def build_card(fig, title="Title", class_name="card-chart-container col-lg-6 md-6 sm-12"):
#     return html.Div(
#         html.Div(
#             className="card-chart",
#             children=[
#                 html.H4(title,
#                         className="card-header card-m-0 me-2 pb-3"),
#                 dcc.Graph(
#                     figure=fig.update_layout(
#                         paper_bgcolor="rgb(0,0,0,0)",
#                         plot_bgcolor="rgb(0,0,0,0)",
#                         legend=dict(bgcolor=theme.LEGEN_BG),
#                         font_family=theme.FONT_FAMILY,
#                     ),
#                     config={"displayModeBar": False},
#                 )
#             ],
#         ), className=class_name
#     )


# winners_card = build_card(title = "World Cup Holders",fig=px.bar(
#     data.groupby("winner", as_index=False).size(),
#     x="winner",
#     y="size",
#     height=theme.MAX_CHART_HEIGHT,
#     text="size",
#     color_discrete_sequence=theme.COLOR_PALLETE,

#     labels={"value": "Country",
#             "size": "Winning Time", "winner": "Winner"},
# ).update_xaxes(categoryorder="total descending"))


# hosts_card = build_card(px.histogram(
#     data["host_country"],
#     color_discrete_sequence=theme.COLOR_PALLETE,
#     height=CARD_HEIGHT,
#     labels={"value": "Country", "size": "Winning Time"},
# ).update_xaxes(categoryorder="total descending",
#                ),title = "hosts_card")


# venues_cities_card = build_card(px.histogram(data, x=data["year"],
#                                              y=["cities", "venues"],
#                                              barmode="group",
#                                              color_discrete_sequence=theme.COLOR_PALLETE,
#                                              height=CARD_HEIGHT,

#                                              ).update_xaxes(type='category'
#                                                             ),title="venues_cities_card")


# total_attendance_card = build_card(px.line(data, x="year",
#                                            y=["total_attendance",
#                                                "avg_attendance"],
#                                            color_discrete_sequence=theme.COLOR_PALLETE,
#                                            height=CARD_HEIGHT,
#                                            ).update_xaxes(type='category'),title="total_attendance_card")


# tours_timeline_card = build_card(px.timeline(data, x_start=data["start_date"].apply(lambda x: "2000" + x[4:]),
#                                              x_end=data["end_date"].apply(lambda x: "2000" + x[4:]), y=data["year"].astype("str"),
#                                              color=(pd.to_datetime(
#                                                  data['end_date'])-pd.to_datetime(data['start_date'])).apply(lambda x: x.days),
#                                              labels={
#     "y": "Year", "color": "Days", "x_start": "Start Date", "x_end": "End Date"},
#     hover_data=["host_country"],
#     color_discrete_sequence=theme.COLOR_PALLETE,
#     color_continuous_scale=theme.COLOR_PALLETE,
# ),title="tours_timeline_card")

# matches_count_card = build_card(px.line(data, x="year", y="matches", color_discrete_sequence=theme.COLOR_PALLETE,).update_xaxes(type="category",
#                                                                                                                                 ),title="matches_count_card")

# most_attended_matches_card = build_card(px.bar(data, x="number", y="year",
#                                                text="game(s)",
#                                                hover_data=["venue", "hosts"],
#                                                orientation="h",
#                                                height=800,
#                                                color_discrete_sequence=theme.COLOR_PALLETE
#                                                ).update_yaxes(type='category'),title="most_attended_matches_card")

# countries_awards_card = build_card(px.histogram(award_winners,
#                                                 x="team_name",
#                                                 color_discrete_sequence=theme.COLOR_PALLETE,
#                                                 ).update_xaxes(
#     categoryorder="total descending"
# ),title="countries_awards_card")


# goals_count_card = build_card(px.line(goals.groupby(
#     "tournament_id", as_index=False).size(), x="tournament_id", y="size", color_discrete_sequence=theme.COLOR_PALLETE,),title="goals_count_card")

# penalties_card = build_card(
#     px.line(goals[goals.penalty == 1].groupby("tournament_id", as_index=False).size(), x="tournament_id", y="size", color_discrete_sequence=theme.COLOR_PALLETE,)
#     ,title="penalties_card")

# goals_per_country_card = build_card(title="goals per country",
# fig=px.bar(goals.groupby("team_name", as_index=False).size(), x="team_name", y="size", color_discrete_sequence=theme.COLOR_PALLETE,
#                                                                           ).update_xaxes(categoryorder="total descending"))


# top_players_df = goals.groupby(["family_name" , "given_name"],as_index=False).size().sort_values(by="size",ascending=False)
# top_players_df.loc[top_players_df["given_name"] == "not applicable" , "given_name"] = ""
# top_players_df["player_full_name"] = top_players_df["given_name"] + " " + top_players_df["family_name"]


# top_players_card = build_card(title="Most acheived goals per player",
# fig=px.bar(top_players_df.head(20),
# y="player_full_name",x="size",
# color_discrete_sequence=theme.COLOR_PALLETE,
# orientation="h").update_yaxes(categoryorder="total ascending"))

# goals_per_minute_card = build_card(
#     title="goals per minute",
# fig=px.line(goals.groupby("minute_regulation",as_index=False).size(),x="minute_regulation",y="size",color_discrete_sequence=theme.COLOR_PALLETE,)
# )

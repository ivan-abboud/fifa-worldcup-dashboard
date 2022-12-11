import plotly.express as px
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc
import utils.theme as theme
from app import tours, goals, award_winners, teams
import numpy as np


def create_card(fig, class_name, title="Title"):
    return html.Div(
        html.Div(
            className="card-chart",
            children=[
                html.H4(title,
                        className="card-header card-m-0 me-2 pb-3", style={"font-size": "1.5vw"}),
                dcc.Graph(
                    figure=fig.update_layout(
                        paper_bgcolor="rgb(0,0,0,0)",
                        plot_bgcolor="rgb(0,0,0,0)",
                        legend=dict(bgcolor=theme.LEGEN_BG),
                        font_family=theme.FONT_FAMILY,
                    ),
                    config={"displayModeBar": False},
                )
            ],
        ), className=class_name
    )


WCWinnersBar = create_card(class_name="card-chart-container col-lg-3 col-md-12 col-sm-12",
                           title="World Cup Holders",
                           fig=px.bar(
                               tours.groupby("winner", as_index=False).size(),
                               x="winner",
                               y="size",
                               height=theme.MAX_CHART_HEIGHT,
                               text="size",
                               color_discrete_sequence=theme.COLOR_PALLETE,
                               labels={"value": "Country",
                                       "size": "", "winner": "Winner"},
                           ).update_xaxes(categoryorder="total descending",
                                          ).update_layout(margin={"r": 20,"l":30}))


tmp_tours = tours
tmp_tours["year"] = tours["year"].astype("str")
HostsCountriesBar = create_card(class_name="card-chart-container col-lg-5 col-md-12 col-sm-12",
                                title="World Cup Hosts",
                                fig=px.bar(tmp_tours.groupby("host_country", as_index=False).agg({"year": " - ".join, "winner": "size"}),
                                           x="host_country", y="winner", text="year",
                                           height=theme.MAX_CHART_HEIGHT,
                                           color_discrete_sequence=theme.COLOR_PALLETE,
                                           labels={
                                               "host_country": "Host Country", "winner": "Hosting Times"}
                                           ).update_xaxes(categoryorder="total descending",
                                                          ).update_layout(margin={"r": 20, "t": 10}))


CountriesTotalGoalsBar = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                                     title="Countries Goals in World Cups (Top 20)",
                                     fig=px.bar(goals.groupby("team_name", as_index=False).size().sort_values(by="size", ascending=False)[:20],
                                                x="team_name", y="size", text_auto=True, color_discrete_sequence=theme.COLOR_PALLETE,
                                                labels={"team_name": "Country", "size": "Goals Count"}, height=theme.MAX_CHART_HEIGHT,
                                                ).update_layout(margin={"r": 20})
                                     )


TotalAttendanceLine = create_card(class_name="card-chart-container col-lg-7 col-md-12 col-sm-12",
                                  title="Total and Average Attendance",
                                  fig=px.line(tours.rename(columns={"total_attendance": "Total", "avg_attendance": "Avg."}),
                                              x="year", y=["Total", "Avg."],
                                              labels={
                                                  "year": "Year", "value": "", "variable": ""},
                                              color_discrete_sequence=theme.COLOR_PALLETE,
                                              height=theme.MAX_CHART_HEIGHT,).update_xaxes(type='category'))

VenuesAndCitiesBar = create_card(class_name="card-chart-container col-lg-5 col-md-12 col-sm-12",
                                 title="Cities and Venues",
                                 fig=px.histogram(tours, x=tours["year"],
                                                  y=["cities", "venues"],
                                                  barmode="group", labels={"year": "Year", "variable": ""},
                                                  color_discrete_sequence=theme.COLOR_PALLETE,
                                                  height=theme.MAX_CHART_HEIGHT,
                                                  ).update_layout(yaxis_title="").update_xaxes(type='category'))


top_players_df = goals.groupby(["family_name", "given_name"], as_index=False).size(
).sort_values(by="size", ascending=False)
top_players_df.loc[top_players_df["given_name"]
                   == "not applicable", "given_name"] = ""
top_players_df["player_full_name"] = top_players_df["given_name"] + \
    " " + top_players_df["family_name"]

TopWcScorersBar = create_card(class_name="card-chart-container col-lg-5 col-md-12 col-sm-12",
                              title="Top Scorers in World Cups",
                              fig=px.bar(top_players_df.loc[top_players_df["size"] > 6],
                                         y="player_full_name", x="size",
                                         labels={"player_full_name": "",
                                                 "size": "Goals Count"},
                                         color_discrete_sequence=theme.COLOR_PALLETE,
                                         height=795,
                                         orientation="h").update_yaxes(categoryorder="total ascending"))

PenaltiesCountPerTour = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                                    title="Penalties Count Per Tour",
                                    fig=px.line(goals[goals.penalty == 1].groupby("year", as_index=False).size(),
                                                x="year", y="size", color_discrete_sequence=theme.COLOR_PALLETE,
                                                height=theme.MAX_CHART_HEIGHT,))


GoalsCountPerTourLine = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                                    title="Goals Count Per Tour",
                                    fig=px.line(goals.groupby(
                                        "year", as_index=False).size(), x="year", y="size",
                                        labels={"year":"Year" , "size":"Count"},
                                        height=theme.MAX_CHART_HEIGHT,
                                        color_discrete_sequence=theme.COLOR_PALLETE,))

CountriesAwardsBar = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                                 title="Countries Total Awards",
                                 fig=px.histogram(award_winners,
                                                  x="team_name",
                                                  labels={
                                                      "team_name": "Team Name"},
                                                  color_discrete_sequence=theme.COLOR_PALLETE,
                                                  height=theme.MAX_CHART_HEIGHT,
                                                  ).update_xaxes(
                                     categoryorder="total descending"
                                 ).update_layout(yaxis_title="Total Awards"))

MostAttendedMatchesBar = create_card(class_name="card-chart-container col-lg-5 col-md-12 col-sm-12",
                                     title="Most Atteneded Match In Each Tour",
                                     fig=px.bar(tours, x="number", y="year",
                                                text="game(s)",
                                                hover_data=["venue", "hosts"],
                                                labels={"number":"Attendance" , "year":"Year"},
                                                orientation="h",
                                                height=795,
                                                color_discrete_sequence=theme.COLOR_PALLETE
                                                ).update_yaxes(type='category'))


tmp_df = pd.DataFrame({"minute": range(121), "count": np.zeros((121))})
grouped_df = goals.groupby("minute_regulation", as_index=False).size()
tmp_df = tmp_df.merge(grouped_df, how="left",
                      left_on="minute", right_on="minute_regulation")
tmp_df["goals_count"] = tmp_df["count"] + tmp_df["size"]
tmp_df.fillna(0, inplace=True)
GoalsCountPerMinute = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                                  title="Goals Count per Minute",
                                  fig=px.line(tmp_df,
                                              x="minute", y="goals_count", labels={"goals_count": "Goals Count", "minute": "Minute"},
                                              color_discrete_sequence=theme.COLOR_PALLETE,
                                              height=theme.MAX_CHART_HEIGHT)
                                  )

MatchesCountBar = create_card(class_name="card-chart-container col-lg-7 col-md-12 col-sm-12",
                              title="Matches Count in Each Tour",
                              fig=px.bar(tours, x="year", y="matches", color_discrete_sequence=theme.COLOR_PALLETE,
                                         height=theme.MAX_CHART_HEIGHT,
                                         text_auto=True,
                                         labels={"matches":"Matches Count", "year":""}
                                         ).update_xaxes(type="category",
                                                        ).update_layout(margin={"r":30}))

ToursTimeline = create_card(class_name="card-chart-container col-lg-5 col-md-12 col-sm-12",
                            title="WorldCups Timeline",
                            fig=px.timeline(tours, x_start=tours["start_date"].apply(lambda x: "2000" + x[4:]),
                                            x_end=tours["end_date"].apply(lambda x: "2000" + x[4:]), y=tours["year"].astype("str"),
                                            color=(pd.to_datetime(
                                                   tours['end_date'])-pd.to_datetime(tours['start_date'])).apply(lambda x: x.days),
                                            labels={
                                "y": "Year", "color": "Days", "x_start": "Start Date", "x_end": "End Date"},
                                height=theme.MAX_CHART_HEIGHT,
                                hover_data=["host_country"],
                                # color_discrete_sequence=theme.COLOR_PALLETE,
                                color_continuous_scale=theme.COLOR_PALLETE[:2],
                                # color_continuous_midpoint=theme.COLOR_PALLETE[0]
                            ))

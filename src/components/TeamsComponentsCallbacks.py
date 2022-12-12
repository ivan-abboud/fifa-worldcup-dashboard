# import plotly.express as px
# import pandas as pd
# from dash import html, dcc
# import utils.theme as theme
# import pandas as pd
# from dash.dependencies import Input, Output, State
# import dash_loading_spinners as dls
# import dash_bootstrap_components as dbc
# from dash import callback


# @callback(
#     Output("team-goals-count-per-tour", "children"),
#     Output("team-ranking-table", "children"),
#     Output("team-goals-count-per-shirt-num", "children"),
#     Output("team-goals-count-per-minute", "children"),
#     Output("team-top-scorers", "children"),
#     Input("query-team-select", "value"),
#     State("goals-df", "data"),
#     State("qualified-teams-df" , "data")
# )
# def update_figures(query_team, goals_df, qualified_teams_df):
#     goals_df = pd.read_json(goals_df)
#     qualified_teams_df = pd.read_json(qualified_teams_df)
#     team_ranking_table = dbc.Table.from_dataframe(qualified_teams_df.loc[qualified_teams_df.team_name == query_team], columns=["year", "performance", "count_matches"],
#                                      header=["Year", "Standing",
#                                              "Matches Count"],
#                                      className=" no-footer", striped=False, bordered=False, hover=True)


#     goals_per_shirt_number = dcc.Graph(figure=px.bar(goals_df.loc[(goals_df.team_name == query_team) & (goals_df.shirt_number != 0)].groupby("shirt_number", as_index=False).size(),
#     x="shirt_number", y="size" , labels={"size":"Goals Count" , "shirt_number":"Shirt Number"} , color_discrete_sequence=theme.COLOR_PALLETE)
#     .update_xaxes(type="category")
#                      .update_layout(paper_bgcolor="rgb(0,0,0,0)",
#                                     plot_bgcolor="rgb(0,0,0,0)",
#                                     legend=dict(
#                                         bgcolor=theme.LEGEN_BG),
#                                     font_family=theme.FONT_FAMILY,
#                                     ),
#                      config={
#         "displayModeBar": False},
#         style=theme.CHART_STYLE

#     )

#     team_tpp_scorers = dcc.Graph(figure=px.bar(goals_df.loc[goals_df.team_name == query_team].groupby("family_name", as_index=False).size().sort_values(by="size", ascending=False).head(10),
#     x="family_name", y="size" , labels={"size":"Goals Count" , "family_name":"Player"} , color_discrete_sequence=theme.COLOR_PALLETE)
#                      .update_layout(paper_bgcolor="rgb(0,0,0,0)",
#                                     plot_bgcolor="rgb(0,0,0,0)",
#                                     legend=dict(
#                                         bgcolor=theme.LEGEN_BG),
#                                     font_family=theme.FONT_FAMILY,
#                                     ),
#                      config={
#         "displayModeBar": False},
#         style=theme.CHART_STYLE

#     )

#     grouped_df = goals_df.loc[goals_df.team_name == query_team].groupby("minute_regulation", as_index=False).size()
#     goals_count_per_minute = dcc.Graph(figure=px.line(grouped_df,
#     x="minute_regulation", y="size", labels={"goals_count":"Goals Count" , "minute": "Minute"} , color_discrete_sequence=theme.COLOR_PALLETE)
#         .update_layout(paper_bgcolor="rgb(0,0,0,0)",
#                        plot_bgcolor="rgb(0,0,0,0)",
#                        legend=dict(
#                            bgcolor=theme.LEGEN_BG),
#                        font_family=theme.FONT_FAMILY,
#                        ),
#         config={
#         "displayModeBar": False},
#         style=theme.CHART_STYLE

#     )

#     qualified_teams_df = qualified_teams_df.loc[qualified_teams_df.team_name == query_team].groupby("year",as_index=False).sum(numeric_only=True)

#     goals_df = goals_df.loc[goals_df.team_name == query_team].groupby(
#         "year", as_index=False).size().merge(qualified_teams_df[["year" , "count_matches"]] , on="year", how="left")
#     goals_df.rename(columns = {'size':'Goals Count' , "count_matches":"Matches Count"}, inplace = True)
    
#     figure = px.line(goals_df, x="year", y=["Goals Count","Matches Count"] , labels={"value":"Count" , "year":"Year", "variable":""}, color_discrete_sequence=theme.COLOR_PALLETE)
    
    

#     return dcc.Graph(figure=figure.
#         update_xaxes(type="category")
#         .update_layout(paper_bgcolor="rgb(0,0,0,0)",
#                        plot_bgcolor="rgb(0,0,0,0)",
#                        legend=dict(
#                            bgcolor=theme.LEGEN_BG),
#                        font_family=theme.FONT_FAMILY,
#                        ),
#         config={
#         "displayModeBar": False},
#         style=theme.CHART_STYLE

#     ), team_ranking_table, goals_per_shirt_number, goals_count_per_minute, team_tpp_scorers
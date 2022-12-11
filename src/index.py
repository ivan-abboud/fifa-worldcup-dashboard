from dash import html, dcc
from components.NavbarVertical import sidebar
from components.BarChartCard import *
from pages.team_analysis import team_analysis_page_content
from dash.dependencies import Input, Output
from app import app, data_store
from components.Footer import Footer
from pages.worldcup_analysis import worldcup_page_content
from pages.about import about_page_content


# page_content = html.Div(
#     className="layout-page container-xxl flex-grow-1 container-p-y pb-0 mt-5",
#     children=[
#         html.Div(id="page-content"),
#     ],
#     style={"padding-top": "70px"}
# )


# app.layout = html.Div(
#     className="layout-wrapper layout-content-navbar",
#     children=[
#         html.Div(
#             className="layout-container",
#             children=[dcc.Location(id="url"),
#                       data_store,
#                       sidebar,
#                       page_content,
#                       html.Footer(className="content-footer footer bg-footer-theme mt-4 ml-0 p-0",
#                                   children=[Footer])
#                       ],
#         ),
#     ],
# )


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
                                                    html.Div(className="container-xxl flex-grow-1 container-p-y",
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


@app.callback(
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




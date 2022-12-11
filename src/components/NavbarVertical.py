from dash import html
import dash_bootstrap_components as dbc



sidebar = html.Div(
    [
        html.Div(
            [
                html.Img(src="./assets/images/ic_world_cup.png", style={"width": "3rem"}),
                html.H4("WorldCup", className="m-0"),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="tf-icons bx bx-trophy fas fa-home"), html.Span("Tournaments" , className="me-2")],
                    href="/",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bx-group"),
                        html.Span("Teams"),
                    ],
                    href="/team-analysis",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bx-info-circle"),
                        html.Span("About"),
                    ],
                    href="/about",
                    active="exact",
                    className="pe-3"
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar bg-menu-theme",
)


# sidebar2 = html.Aside(
#     className="aside aside-left d-flex aside-fixed layout-menu menu-vertical menu bg-menu-theme col-lg-6",
#     children=[
#         html.Div(
#             className="app-brand demo",
#             children=[
#                 html.Span(
#                     html.Img(
#                         src="./assets/images/logo-no-name.png",
#                         height="38px",
#                         style={"margin": "16px 0px", "margin-right": "10px"},
#                     )
#                 )
#             ],
#             style={"padding": 0, "margin": 23}
#         ),
#         dbc.Nav(
#             [
#                 html.Div(className="menu-inner-shaddow"),
#                 html.Ul(
#                     className="menu-inner",
#                     children=[
#                         html.Li(
#                             id="overview-item",
#                             className="menu-item",
#                             children=[
#                                 dbc.NavLink(
#                                     children=[
#                                         html.I(
#                                             className="menu-icon tf-icons bx bxs-home"
#                                         ),
#                                         "OCR+",
#                                     ],
#                                     href="/",
#                                     className="menu-link",
#                                     active="exact",
#                                     #style={"width": 50}
#                                 ),
#                             ], #style={"width": "auto"}
#                         ),
#                         dbc.NavItem(
#                             id="second-item",
#                             className="menu-item",
#                             children=[
#                                 dbc.NavLink(
#                                     children=[
#                                         html.I(
#                                             className="menu-icon tf-icons bx bx-laptop"
#                                         ),
#                                         "Demo",
#                                     ],
#                                     href="/second-page",
#                                     className="menu-link",
#                                     active="exact",
#                                     style={"width": 50}
#                                 ),
#                             ],
#                         ),
#                         dbc.NavItem(
#                             id="third-item",
#                             className="menu-item",
#                             children=[
#                                 dbc.NavLink(
#                                     children=[
#                                         html.I(
#                                             className="menu-icon tf-icons bx bx-line-chart"
#                                         ),
#                                         "Statistics",
#                                     ],
#                                     href="/third-page",
#                                     className="menu-link",
#                                     active="exact",
#                                     style={"width": 50}
#                                 ),
#                             ],
#                         ),
#                     ],
#                     style={ "margin-top": "30px"}
#                 ),
#             ],
#             vertical=True,
#         ),
#     ], #style={"width": 200}
# )

# navbar = dbc.Navbar(
#     [
#         html.A(
#             dbc.Row(
#                 [
#                     dbc.Col(html.Img(alt="Fifa WorldCup 2022", src="./assets/lisan-logo.png", height="60px",style={"margin-left":"60px"}),class_name=""),
                    
#                     dbc.Col(dbc.NavItem(dbc.NavLink("Logo Similarity", active=True, href="/")),class_name="",style={"width":"250px"}),
#                     dbc.Col(dbc.NavItem(dbc.NavLink("Name Similarity", href="/name-similarity")),class_name="" )

#                     ,
                    
#                     #dbc.Col(dbc.NavbarBrand("Trademark Infringement Detector", className="ml-2")),
#                 ],
#                 align="center",
                
#             ),
#             href="https://lisan.ai/",
#             style={}
#         ),
#     ],
#     color="#fff",
#     dark=False,
#     fixed=True,
# )
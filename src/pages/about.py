from dash import html
import utils.theme as theme
about_me_text= "Data scientist with 2+ years of experience in building data-intensive applications, overcoming complex challenges in multiple industries, Proficient in predictive data modeling, processing, visualizing, and extracting actionable insights from data"

about_page_content = html.Div(className="col-md-12 col-sm-12 col-lg-8 mb-md-0 mb-4 card-chart-container", children=[html.Div(className="card", children=[
        html.Div(className="card-body p-0", children=[
            html.Div(className="d-flex justify-content-between", children=[
                html.Div(className="card-info p-4 w-75",
                         children=[html.H3(className="card-text", children=["Who am I?"]),
                                    html.H2(className="card-text m-0 p-0", children=["Ivan Abboud"] , style={"color":theme.COLOR_PALLETE[0]}),
                                   html.Div(className="mb-2 mt-2", children=[
                                       html.Small(className="card-title mb-2",
                                            children=[about_me_text], style={"font-size":"1rem"}),
                                   ]),
                                   html.Small(
                             className="card-text", children=["call me"]
                         )
                         ]),
                html.Div(className="card-icon d-flex align-items-end", children=[
                    html.Img(className="img-fluid",
                             src="./assets/images/programmer.gif" , style={"border-radius":6})
                ]
                )
            ])

        ])
    ])
    ]
    )
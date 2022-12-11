from dash import html

def CardWithIcon(icon, card_header, card_body, card_tail,class_name=""):
    return html.Div(className="col-md-6 col-lg-6 mb-md-0 mb-4 " + class_name, children=[html.Div(className="card", children=[
        html.Div(className="card-body", children=[
            html.Div(className="d-flex justify-content-between", children=[
                html.Div(className="card-info",
                         children=[html.Small(className="card-text", children=[card_header]),
                                   html.Div(className="mb-2 mt-2", children=[
                                       html.H2(className="card-title mb-2",
                                            children=[card_body], style={"font-size":"2vw"}),
                                   ]),
                                   html.Small(
                             className="card-text", children=[card_tail]
                         )
                         ]),
                html.Div(className="card-icon d-flex align-items-center", children=[
                    html.Img(className="img-fluid bx-lg fi",
                             src=icon,style={"box-shadow": "0 2px 6px 0 rgb(67 89 113 / 20%)"})
                ]
                )
            ])

        ])
    ])
    ]
    )
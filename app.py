import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output, State

app = dash.Dash()

header = html.Div([
    dcc.Location(id='logout_url', refresh=True),
    #html.Img(src=app.get_asset_url("logo.png"), id="logo"),
    html.Div(id="header_text"),
    html.Button("Logout", id="logout_button"),
    html.Div([
        html.Img(id="profile_logo")
    ], id="profile_div")
], id="header", style={'textAlign': 'right',
                       'margin': '48px 0',
                       'fontFamily': 'system-ui'})

footer = html.Div([
    html.Div("2019", id="footer_text")
], id="footer")

app.layout = \
    html.Div([
        html.H1('Dash Tabs component demo',
                style={'textAlign': 'center',
                       'margin': '48px 0',
                       'fontFamily': 'system-ui'}),
        header,
        html.Div([
            html.Div([
                dcc.Tabs(id="tabs",
                         vertical=True,
                         parent_style={'flex-direction': 'column',
                                       '-webkit-flex-direction': 'column',
                                       '-ms-flex-direction': 'column',
                                       'display': 'flex'},
                         children=[dcc.Tab(label='Tab one', value='1'),
                                   dcc.Tab(label='Tab two', value='2'),
                                   dcc.Tab(label='Tab three', value='3')])],
                     style={'width': '25%',
                            'float': 'left'}),
            html.Div(id='tab-out',
                     style={'width': '75%', 'float': 'right'}),
        ]),

        footer, ], style={'flex-direction': 'column',
                          '-webkit-flex-direction': 'column',
                          '-ms-flex-direction': 'column',
                          'display': 'flex'})


@app.callback(Output('tab-out', 'children'),
              [Input('tabs', 'value')])
def tab_content(tabs_value):
    """return s.th. based on tabs_value"""
    if tabs_value == '3':

        children = [
            html.Div([
                html.H1("This is the content in tab 3"),
            ])
        ]
    elif tabs_value == '2':
        children = [
            html.Div([
                html.H1("This is the content in tab 2"),
                html.P("A graph here would be nice!"),
                dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2],
                             'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5],
                             'type': 'bar', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'title': 'Dash Data Visualization'
                        }
                    }
                ),
            ])
        ]
    else:
        children = html.Div([
            dcc.Graph(
                id='example-graph1.1',
                figure={
                    'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2],
                                'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5],
                             'type': 'bar', 'name': u'Montréal'},
                            ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            ),
            dcc.Graph(
                id='example-graph1.2',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2],
                         'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5],
                         'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
        ])

    return children


if __name__ == '__main__':
    app.run_server(debug=True)

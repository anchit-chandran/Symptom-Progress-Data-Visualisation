from figs import make_csbm_bsc_fig_function, make_sms_fig, make_dact_fig
from dfs import clean_df, make_csbm_df_function,make_sms_df,make_dact_df_function

from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output# Load Data

qipidlist = clean_df().QIPID.unique().tolist()
qipidlist.append('ALL')

#TITLE
title_card_component = dbc.Col([

    html.H1("Quality Improvement PURA Dashboard",
                className='pt-2'),
            
    html.H4("Made by Dr Anchit Chandran",
                className='')

], className='bg-primary text-center mt-3 p-3', width={'size':5})

#DROPDOWN SELECT QIPID
qipid_selector_component = dbc.Col([
                                    
    dbc.Card(dbc.CardBody([
        
        html.H2("Select QIPID: ", className='card-title'),

        dcc.Dropdown(
            id='qipid_dropdown',
            options= [{'label': qipid, 'value': qipid} for qipid in qipidlist],
            value= qipidlist[-1],
            clearable=False,
        )

    ]))
                                    
], className='p-3', width={'size':2})



# GENERAL INFO
general_info_component = dbc.Col([
    dbc.Card(dbc.CardBody([

        html.H2("General info", className='card-title'),

        # First example - using dbc.PopoverBody
        dbc.Button(
            "Number of Dropped Data Points",
            id="popover-target",
            className="me-1",
        ),
        dbc.Popover(
            dbc.PopoverBody([
                html.P(id='general_info_output_csbm'),
                html.P(id='general_info_output_sms'),
                html.P(id='general_info_output_dact')
            ]),
            target="popover-target",
            trigger="hover",
        ),

    ]), className='border-primary')
], className='pt-3', width={'size':3})




# CSBM GRAPH 
csbm_component = dbc.Col([       
                                                
    dbc.Card([dbc.CardBody([
                                
                html.H5('💩 Complete Spontaneous BMs & Bristol Stool Score', className='text-center p-1'),

                dcc.Graph(
                    id='csbm_graph',
                    figure= make_csbm_bsc_fig_function(make_csbm_df_function()[0])
                ),

                #OUTPUT DIV, CSBM
                html.Div(
                        id='output_div_csbm'
                        )
            
            ],className='',

        )])
          
], className='p-3', width=5)

#ST MARKS GRAPH COMPONENT
sms_component = dbc.Col([

    dbc.Card([dbc.CardBody([

        html.H5("💩 St Mark's Score", className='text-center p-1'),

        dcc.Graph(
            id='sms_graph',
            figure=make_sms_fig(make_sms_df()[0])
        ),

        # OUTPUT DIV, SMS
        html.Div(id='output_div_sms')

    ], className='')])


], className='p-3', width=5)


daily_activity_component = dbc.Col([

    dbc.Card([dbc.CardBody([

        html.H5(
            "💩 Daily Activity Score (8 day rolling)", className='text-center p-1'),

        dcc.Graph(
            id='dact_graph',
            figure=make_dact_fig(make_dact_df_function()[0])
        ),

        # OUTPUT DIV, daily adctivities
        html.Div(id='output_div_dact')

    ], className='')])


], className='p-3', width=5)



################################

# RUN DASH APP

#################################

app = Dash(__name__, external_stylesheets=[dbc.themes.UNITED],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}
                           ]
                  )

app.layout = dbc.Container([
                dbc.Row([
                         title_card_component,
                         qipid_selector_component,
                         general_info_component
                    ], justify='center', align='start'),
                
                dbc.Row([
                         csbm_component,
                         sms_component,
                         daily_activity_component,

                ], justify='center', align='stretch'),
                
], fluid=True)

@app.callback(
    Output('csbm_graph','figure'),
    Output('sms_graph', 'figure'),
    Output('dact_graph','figure'),
    Output('general_info_output_csbm','children'),
    Output('general_info_output_sms','children'),
    Output('general_info_output_dact','children'),
    Input('qipid_dropdown','value')
)
def update_graph(qipid):

    csbm_fig = make_csbm_bsc_fig_function(make_csbm_df_function(qipid)[0])
    sms_fig = make_sms_fig(make_sms_df(qipid)[0])
    dact_fig = make_dact_fig(make_dact_df_function(qipid)[0])

    csbm_dropped = f"Dropped {make_csbm_df_function(qipid)[1]} from CSBM due to NA"
    sms_dropped = f"Dropped {make_sms_df(qipid)[1]} from St Mark's due to NA"
    dact_dropped = f"Dropped {make_dact_df_function(qipid)[1]} from Daily Activity due to NA"

    return (csbm_fig,
            sms_fig,
            dact_fig,
            csbm_dropped,
            sms_dropped,
            dact_dropped
            )



#RUN DASH APP
app.run_server(port=333, debug=True)
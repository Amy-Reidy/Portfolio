# importing necessary libraries

import numpy as np
import pandas as pd

#Plotly
import plotly
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.io as pio

# Dash
import dash
from dash import dcc
from dash import html
from jupyter_dash import JupyterDash
from dash.dependencies import Input, Output

import flask

pio.templates.default = "plotly_white"

df_countries3 = pd.read_csv('data/cervical_cancer_global_data.csv')

x_features = ['Human Development Index (HDI)', 'Life Expectancy at Birth',
       'Expected Years of Schooling', 'Mean Years of Schooling',
       'Gross National Income (GNI) per Capita', 'Incidence', 'Mortality']

y_features = ['Incidence', 'Mortality']

markdown_text = '''

Dashboard created by [Amy Reidy](https://www.linkedin.com/in/amy-reidy1/).

*Incidence* = Age-Standardized Incidence Rate per 100,000 in 2020  |  *Mortality* = Age-Standardized Mortality Rate per 100,000 in 2020

*National HPV Vaccination Programs* = Countries which had national HPV vaccination programs as of 17th August 2021. 

Data Sources: [Global Cancer Observatory](https://gco.iarc.fr/) (CC rates),  [PATH](https://www.path.org/) (list of national HPV vaccine programs) and [United Nations Development Programme](https://www.undp.org/) (HDI and component indicators)



'''
# Dash Instance --------------------------------------------------------------------------------------
server = flask.Flask(__name__) # define flask app.server
app = dash.Dash(__name__, server=server)
app.title = 'Global Disparities in Cervical Cancer Rates'



########################### Dashboard Layout ################################################################################
app.layout = html.Div([
        html.Div([html.H1('Global Disparities in Cervical Cancer Rates',style={
                                                             'text-align': 'center',
                                                            'margin-top': '10px', 'margin-bottom': '10px', 'color': '#570A8C'})]),
        html.Div(children=[
            html.Div(children=[
                html.H4('CC Rate: ', style={'display': 'inline-block'}),
                dcc.RadioItems(id='main_ind', options=[{'label': i.title(), 'value': i} for i in y_features], value='Incidence', inputStyle={"margin-left": "10px"}, style={'display': 'inline-block'})]
                    , style={'width': '45%', 'text-align': 'right','color': '#570A8C', 'display': 'inline-block','font-size': '20px'}),                                     
        
            html.Div(children=[
                html.H4('Geographical Area: ', style={'display': 'inline-block'}),
                dcc.RadioItems(id='geo_ind', options=[
                                {'label': 'Continent', 'value': 'Continent'},
                                {'label': 'Sub-Region', 'value': 'Sub-Region'}], 
                                value='Continent', style={'display': 'inline-block'},
                                inputStyle={"margin-left": "10px"}),]
                    , style={'width': '40%', 'margin-left': '60px', 'text-align': 'left','color': '#570A8C', 'display': 'inline-block','font-size': '20px'}),                                     
             ]),                                                             
    

        html.Div(children=[
            html.Div(children=[
                    dcc.Graph(id='sunburst-chart',style={'border': '0px solid #cfcfcf'}, config={'displayModeBar': False})
            ],style={'text-align': 'center','display': 'inline-block','width': '40%'}),
                         
                             
            html.Div(children=[ 
                    dcc.Graph(id='bar-graph',style={'border': '0px solid #cfcfcf'}, config={'displayModeBar': False}),   
            ],style={'text-align': 'center','display': 'inline-block','width': '60%'} ),                     
        ]),
    

        html.Div(children=[

            html.Div(children=[
                    dcc.Graph(id='map-chart', style={'border': '0px solid #cfcfcf'}),   
                ],style={'display': 'inline-block','width': '48%'}),
                             
            html.Div(children=[
                    dcc.Graph(id='scatter-plot',style={'border': '0px solid #cfcfcf'}, config={'displayModeBar': False}),
                    dcc.Dropdown(id='xaxis', options=[{'label': i, 'value': i} for i in x_features], 
                                 value='Human Development Index (HDI)', style={'text-align': 'center','display': 'inline-block','width': '100%'}),
                ], style={'width': '50%', 'display': 'inline-block'}),
         ]),    
        html.Br(),
        html.Div(children=[
                    dcc.Markdown(markdown_text)
                ], style={'text-align': 'center'}),   

             ],style={'border': '1px solid #cfcfcf'})

########################### Callbacks for Interactive Graphs ###############################################################################


# Fig. 1 Sunburst plot

@app.callback(
    Output('sunburst-chart', 'figure'),
    [Input('geo_ind', 'value'),
    Input('main_ind', 'value')])
def update_sun(geo_id, main_ind):
    fig = px.sunburst(df_countries3, 
                    path=[geo_id, 'Country'],
                    color=df_countries3[main_ind], 
                    values=df_countries3[main_ind],
                    color_continuous_scale="bluered",
                    color_continuous_midpoint=round(np.average(df_countries3[main_ind]),2),
                    #hover_name=main_ind, 
                    #hover_data={main_ind:':.2f'},
                    custom_data=[main_ind]
                     )
    #fig.update_traces(hoverinfo="label+name", selector=dict(type='sunburst'))
    #fig.update_traces(hovertemplate="<b>Incidence</b>: %{customdata[0]:.2f}<br><br>")
    fig.update_layout(title_text='<b>Click on {} for {} Rates by Country</b>'.format(geo_id, main_ind), title_x=0.5)
    fig.update_layout(margin={"r":0,"t":80,"l":0,"b":0})
    fig.update_coloraxes(showscale=False) 
    
    return fig
 
# Fig. 2 Bar Graph   
    
@app.callback(
    Output('bar-graph', 'figure'),
    [Input('geo_ind', 'value'),
    Input('main_ind', 'value')])
def update_bar(geo_ind, main_ind):
    fig = px.bar(df_countries3.groupby(geo_ind).mean()[main_ind], 
                color=df_countries3.groupby(geo_ind).mean()[main_ind],
               color_continuous_scale="bluered",
               opacity=0.6,
                text_auto='.1f',
                )
    fig.update_layout(title_text='<b>{} Rates by {}</b>'.format(main_ind, geo_ind), title_x=0.5)
    fig.update_xaxes(categoryorder='total ascending')
    fig.update_xaxes(tickangle=45)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(margin={"r":0,"t":80,"l":0,"b":0})
    fig.update_traces(hovertemplate=None, hoverinfo='skip')
    fig.update_layout(xaxis=dict(tickfont=dict(size=10), title=''), yaxis=dict(title='Average {} Rate'.format(main_ind)))
    
    return fig


# Fig 3. Map

@app.callback(
    Output('map-chart', 'figure'),
    [Input('main_ind', 'value')])
def update_map(main_ind):
    fig = px.scatter_geo(df_countries3,
            locations="Code3",
            color=main_ind,
            size=main_ind,
            color_continuous_scale="bluered",
            hover_name="Country", hover_data={main_ind:True, 'National HPV Vaccination Program':True, 'Sub-Region':True, 'Code3':False}
                )
        
    fig.update_layout(margin={"r":30,"t":0,"l":30,"b":0})
    #fig.update_coloraxes(showscale=False) 
    #fig.update_coloraxes(colorbar_ticklabelposition="inside bottom")

    return fig  




# Fig. 4 Scatter Plot  
    

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('xaxis', 'value'),
     Input('main_ind', 'value')])
def update_graph(xaxis_name, main_ind):
        fig = px.scatter(df_countries3,
            x=xaxis_name,
            y=main_ind,
            color=df_countries3['National HPV Vaccination Program'],
            size=main_ind,
            color_discrete_map={"Yes": "MediumPurple", "No": "Red"},
            opacity=0.7,
            trendline='ols',
            hover_name="Country", hover_data={main_ind:True, xaxis_name:True}
        )
        
        fig.update_layout(title_text='<b>{} Vs. {}</b> (click x-axis to change)'.format(main_ind, xaxis_name), title_x=0.5)        
        fig.update_layout(margin={"r":20,"t":100,"l":0,"b":0})
        fig.update_layout(legend=dict(
                title="National HPV Vaccination Program?",
                yanchor="top",
                y=0.99,
                xanchor="right",
                x=0.99))
        fig.update_layout(yaxis=dict(tickfont=dict(size=10)))
        fig.update_layout(xaxis=dict(tickfont=dict(size=10), title=''))
              
        return fig

if __name__ == '__main__':
    app.run_server(debug=False)

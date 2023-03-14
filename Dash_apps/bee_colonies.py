import pandas as pd
import numpy as np 
import plotly.express as px 
import chart_studio.plotly as py 
import cufflinks as cf
import seaborn as sns
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot 
import dash 
from dash import dcc  
from dash import html 
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc 
import plotly.graph_objects as go
init_notebook_mode(connected=True)
cf.go_offline()

# Let's get the dataset first and clean it up 

original_df = pd.read_csv('/home/giorgio/python/Notebooks/Plotly/Dash/Data/bees.csv')

groupby = ['State', 'ANSI', 'Affected by', 'Year', 'state_code']
groupto = 'Pct of Colonies Impacted'

def clean_dataframe(dataframe, groupby_list, groupto, index_inplace=True):
    df = dataframe.copy()
    df = df.groupby(groupby_list)[groupto].mean().to_frame()
    df.reset_index(inplace=index_inplace)
    return df 

clean_df = clean_dataframe(original_df, groupby_list=groupby, groupto=groupto)

# Useful variables for later 

years_dictionary = [
    {'label': '2015', 'value': 2015},
    {'label': '2016', 'value': 2016},
    {'label': '2017', 'value': 2017},
    {'label': '2018', 'value': 2018},
    {'label': '2019', 'value': 2019},
]

colormap_dictionary = [
    {'label': 'Greys', 'value': 'Greys'},
    {'label': 'YlGnBu', 'value': 'YlGnBu'},
    {'label': 'Greens', 'value': 'Greens'},
    {'label': 'YlOrRd', 'value': 'YlOrRd'},
    {'label': 'Bluered', 'value': 'Bluered'},
    {'label': 'RdBu', 'value': 'RdBu'},
    {'label': 'Reds', 'value': 'Reds'},
    {'label': 'Blues', 'value': 'Blues'},
    {'label': 'Picnic', 'value': 'Picnic'},
    {'label': 'Rainbow', 'value': 'Rainbow'},
    {'label': 'Portland', 'value': 'Portland'},
    {'label': 'Jet', 'value': 'Jet'},
    {'label': 'Hot', 'value': 'Hot'},
    {'label': 'Blackbody', 'value': 'Blackbody'},
    {'label': 'Earth', 'value': 'Earth'},
    {'label': 'Electric', 'value': 'Electric'},
    {'label': 'Viridis', 'value': 'Viridis'},
    {'label': 'Cividis', 'value': 'Cividis'},
    {'label': 'Magma', 'value': 'Magma'},
    {'label': 'Plasma', 'value': 'Plasma'},
    {'label': 'Inferno', 'value': 'Inferno'}, 
    {'label': 'Turbo', 'value': 'Turbo'}]


# Let's start the app 

app = dash.Dash(__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP])

# Let's create a layout for the webapp

app.layout = html.Div([

    html.H1('Bees affected by Varroa Mites in the US', style={'text-align': 'center'}), 

    dcc.Dropdown(id='selected_year',
        options= years_dictionary,
        value=2015,
        multi=False,
        style = {'width': '40%'}
    ), 

    dcc.Dropdown(id='Colormap',
        options=colormap_dictionary,
        value='Plasma',
        multi=False, 
        style = {'width': '70%'}
    ), 

    html.Div(id = 'output_container', children = []), 
    html.Div(id = 'colormap_selection', children = []),
    html.Br(),

    dcc.Graph(id = 'map', figure = {})
])

# Let's create an app callback to define the outputs and inputs that will update the layout

@app.callback(
    [Output(component_id = 'output_container', component_property = 'children'), 
     Output(component_id = 'map', component_property = 'figure'), 
     Output(component_id = 'colormap_selection', component_property = 'children')], 

    [Input(component_id = 'selected_year', component_property = 'value'), 
     Input(component_id = 'Colormap', component_property = 'value')]
)

def update_map(selection, Colormap=colormap_dictionary):

    container = 'The year chosen by user was: {}'.format(selection)

    dff = clean_df.copy()
    dff = dff[dff['Year'] == selection]
    dff = dff[dff['Affected by'] == 'Varroa_mites']

    # Creating the figure with plotly express 

    fig = px.choropleth(data_frame=dff, locationmode='USA-states', locations='state_code', 
                        color=groupto, scope='usa', color_continuous_scale=Colormap, 
                        hover_data=['State', groupto], 
                        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
                        template='plotly_dark')
    fig.update_layout(height=600)

    return container, fig, Colormap
    
    # Run the app

if __name__ == '__main__':
    app.run()

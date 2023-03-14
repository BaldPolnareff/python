import pandas as pd
import numpy as np 
import plotly.express as px 
import chart_studio.plotly as py 
import cufflinks as cf
import seaborn as sns
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot 
from dash import Dash  
from dash import dcc  
from dash import html 
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc 
import plotly.graph_objects as go
cf.go_offline()

# importing from local files 

from components.layout import create_layout

# A colormap dictionary that I might need later
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

# main 

def main() -> None:
    # creating the app itself
    app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
    # defining a layout and a title
    app.title = 'Mahmood Soldi Dashboard'
    app.layout = create_layout(app)

    # app execution
    app.run()

if __name__ == "__main__":
    main()
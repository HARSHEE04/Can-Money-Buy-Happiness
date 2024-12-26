#This file is used for the callback and serves as the connection between the components and the logic

from dash import Dash, dcc, Output, Input #output and input are libraries used for callback
import dash_bootstrap_components as dbc  


app= Dash(__name__,external_stylesheets=[dbc.themes.SOLAR]) #again used to start our app and choose a theme, SOLAR is a darker theme

#need to define components, inputs and output and callback function
#in the callback function, the arguments are the components property of the input
#the return is assigned to the component property of the output

#may have to define multiple callbacks then?
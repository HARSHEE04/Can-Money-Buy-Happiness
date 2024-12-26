from dash import Dash, dcc 
import dash_bootstrap_components as dbc
import Logic


#set up the page]
app= Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP]) #stays consistant

#can create variable and then use markdown which appears as H1 header

myTitle= dcc.Markdown(children="The Real Price of Joy: Does Money Buy Happiness?")

#make layout, put components inside layout
app.layout=dbc.Container([myTitle])
 


#

if __name__=='__main__':
    app.run_server(port =8051) #Dash is based on flask programming and you can call this to call the main method which is the starting point of programs in Python

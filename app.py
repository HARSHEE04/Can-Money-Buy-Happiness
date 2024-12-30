from dash import Dash, dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.graph_objects as obj
import plotly.express as px
from Logic import df

# Initialize the app with Bootstrap
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Scatter Plot
scatter_plot = px.scatter(
    df,
    x="GDP",
    y="life_ladder",
    color="country_name",
    title="GDP VS Life Ladder Score",
    labels={"GDP": "Log GDP per Capita", "life_ladder": "Life Ladder (%)"},
    hover_name="country_name"
)
scatter_plot.update_layout(
    title_font=dict(size=20),
    xaxis_title_font=dict(size=16),
    yaxis_title_font=dict(size=16),
    template="plotly"
)

# Line Graph
line_graph = px.line(
    df,
    x="year",  # Example Year column
    y="life_ladder",  # Example Happiness column
    color="country_name",  # Different lines based on country_name
    title="Happiness Over Time",
    labels={"year": "Year", "life_ladder": "Life Ladder (%)"}
)
line_graph.update_layout(
    title_font=dict(size=20),
    xaxis_title_font=dict(size=16),
    yaxis_title_font=dict(size=16),
    template="plotly",
    legend_title="Country"  # Set legend title
)

#Bubble Chart
bubble_graph= px.scatter(df,
    x="GDP",
    y="life_ladder",
    size="life_ladder",
    color="country_name",
    title="GDP VS Life Ladder Score",
    labels={"GDP": "Log GDP per Capita", "life_ladder": "Life Ladder (%)"},
    hover_name="country_name")

bubble_graph.update_layout ( 
    title_font=dict(size=20),
    xaxis_title_font=dict(size=16),
    yaxis_title_font=dict(size=16),
    template="plotly",
    legend_title="Country"  # Set legend title
)
# Navigation Bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Scatter Plot", href="/scatter")),
        dbc.NavItem(dbc.NavLink("Line Graph", href="/line")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Bubble Chart", href="/bubble"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Explore Visualizations",
    brand_href="/",
    color="purple",
    dark=True,
)

# Main layout
app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),  # URL tracking component
    myTitle := dcc.Markdown(children="The Price of Joy: Does Money Buy Happiness?", style={"fontSize": "4vw"}),
    myHeading := dcc.Markdown(children="An end-to-end data analysis project investigating the link between wealth and happiness - HS", style={"fontSize": "2vw"}),
    navbar,
    html.Div(id='page-content')  # Placeholder for page content
])

# Callback to render pages based on URL
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/scatter':
        return scatter_page
    elif pathname == '/line':
        return line_page
    elif pathname=='/bubble':
        return bubble_page 
    else:
        return scatter_page  # Default to scatter page

# Scatter page layout
scatter_page = html.Div([
    dcc.Markdown(children="## GDP vs Life Ladder Score"),
    dcc.Graph(figure=scatter_plot)
])

# Line page layout
line_page = html.Div([
    dcc.Markdown(children="## Happiness Over Time"),
    dcc.Graph(figure=line_graph)
])

#bubble chart page layout

bubble_page= html.Div([
    dcc.Markdown (children="## Effects of GDP on Happiness"),
    dcc.Graph(figure=bubble_graph)
    ])


if __name__ == '__main__':
    app.run_server(port=8051)

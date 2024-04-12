from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go

df = px.data.gapminder()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

color_sequence = px.colors.qualitative.Set1 # Define a color sequence

app.layout = html.Div([

    dcc.Dropdown(id='dpdn2', value=['Germany','Brazil'], multi=True, options=[{'label': x, 'value': x} for x in df.country.unique()]),
    html.Div([
        dcc.Graph(id='pie-graph', figure={}, className='six columns'),
        dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None,
                  config={
                      'staticPlot': False,     # True, False
                      'scrollZoom': True,      # True, False
                      'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                      'showTips': False,       # True, False
                      'displayModeBar': False,  # True, False, 'hover'
                      'watermark': True,
                      # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                        },
                  className='six columns'
                  ),
        dcc.Graph(id='bar-chart', figure={}, className='six columns')  # Add a third chart for the bar chart
    ])
])

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='dpdn2', component_property='value'),
)
def update_graph(country_chosen):
    dff = df[df.country.isin(country_chosen)]
    fig = px.line(data_frame=dff, x='year', y='gdpPercap', color='country',  hover_data=["lifeExp", "pop", "iso_alpha"], color_discrete_sequence=color_sequence)
    fig.update_traces(mode='lines+markers')
    return fig

@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
    Input(component_id='dpdn2', component_property='value')
)
def update_side_graph(hov_data, country_chosen):
    if hov_data is None:
        dff2 = df[df.country.isin(country_chosen)]
        dff2 = dff2[dff2.year == 1952]
        fig2 = px.pie(data_frame=dff2, values='pop', names='country',
                      title='Population for 1952', color='country', color_discrete_sequence=color_sequence)
        return fig2
    else:
        hov_year = hov_data['points'][0]['x']
        dff2 = df[df.country.isin(country_chosen)]
        dff2 = dff2[dff2.year == hov_year]
        fig2 = px.pie(data_frame=dff2, values='pop', names='country', title=f'Population for: {hov_year}', color='country', color_discrete_sequence=color_sequence)
        return fig2

@app.callback(
    Output(component_id='bar-chart', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
    Input(component_id='dpdn2', component_property='value')
)
def update_bar_chart(hov_data, country_chosen):
    if hov_data is None:
        dff3 = df[df.country.isin(country_chosen)]
        dff3 = dff3[dff3.year == 1952]
        fig3 = px.bar(data_frame=dff3, x='country', y='pop', title='Population for 1952', color='country', color_discrete_sequence=color_sequence)
        return fig3
    else:
        hov_year = hov_data['points'][0]['x']
        dff3 = df[df.country.isin(country_chosen)]
        dff3 = dff3[dff3.year == hov_year]
        fig3 = px.bar(data_frame=dff3, x='country', y='pop', title=f'Population for: {hov_year}', color='country', color_discrete_sequence=color_sequence)
        return fig3

if __name__ == '__main__':
    app.run_server(debug=True)

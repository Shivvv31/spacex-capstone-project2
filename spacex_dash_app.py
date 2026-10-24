# SpaceX Launch Records Dashboard (Plotly Dash)
# wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
sites = sorted(spacex_df['Launch Site'].unique())

app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    # TASK 1: launch site dropdown
    dcc.Dropdown(id='site-dropdown',
                 options=[{'label': 'All Sites', 'value': 'ALL'}] + [{'label': s, 'value': s} for s in sites],
                 value='ALL', placeholder='Select a Launch Site here', searchable=True),
    html.Br(),
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),
    html.P("Payload range (Kg):"),
    # TASK 3: payload range slider
    dcc.RangeSlider(id='payload-slider', min=0, max=10000, step=1000,
                    marks={i: str(i) for i in range(0, 10001, 2500)},
                    value=[min_payload, max_payload]),
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# TASK 2: pie chart callback
@app.callback(Output('success-pie-chart', 'figure'),
              Input('site-dropdown', 'value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        return px.pie(spacex_df, values='class', names='Launch Site',
                      title='Total successful launches by site')
    filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
    counts = filtered_df.groupby('class').size().reset_index(name='count')
    return px.pie(counts, values='count', names='class',
                  title=f'Total success vs. failure launches for site {entered_site}')

# TASK 4: scatter chart callback
@app.callback(Output('success-payload-scatter-chart', 'figure'),
              [Input('site-dropdown', 'value'), Input('payload-slider', 'value')])
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)]
    if entered_site != 'ALL':
        df = df[df['Launch Site'] == entered_site]
    return px.scatter(df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                      title='Correlation between payload and success for ' +
                            ('all sites' if entered_site == 'ALL' else entered_site))

if __name__ == '__main__':
    app.run(port=8050)

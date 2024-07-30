from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px


# Incorporate data
df = pd.read_csv('data/Wii_final.csv')
df = df.drop('Unnamed: 0', axis=1)


# Initialize the app
app = Dash(__name__)

# App layout
app.layout = [html.Div(children='Fallguard: Fall detection in the elderly'),
              html.Hr(),
              dcc.RadioItems(options=['avg_grip_strength', 'walking_difficulty', 'reaching_overhead_difficulty'], value='avg_grip_strength', id='controls-and-radio-item'),
              dcc.Graph(figure={}, id='controls-and-graph'),
              dcc.Graph(figure=px.scatter(df, x='age', y='avg_grip_strength', color='gender')),
              dash_table.DataTable(data=df.to_dict('records'), page_size=6)
]

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)

def update_graph(col_chosen):
    fig = px.bar(df, x='has_fell', y=col_chosen)
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

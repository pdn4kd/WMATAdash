'''Putting together a ridership dashboard'''
from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

# Initialize the app
app = Dash()

# Incorporate data
df = pd.read_csv('WMATA202601.csv')

# App layout
app.layout = [
	html.Div(children='WMATA Metrobus ridership (January 2026)'),
	html.Hr(),
	dcc.Graph(figure={}, id='controls-and-graph'),
	dcc.RadioItems(options=['Weekday', 'Saturday', 'Sunday', 'Total'], value='Weekday', id='controls-and-radio-item'),
	html.Hr(),
	dag.AgGrid(
		rowData=df.to_dict('records'),
		columnDefs=[{"field": i} for i in df.columns]
	)
]

# Add controls to build the interaction
@callback(
	Output(component_id='controls-and-graph', component_property='figure'),
	Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(val_chosen):
	xs = val_chosen + "Boardings"
	ys = val_chosen + "Paid"
	fig = px.scatter(df, xs, ys, color="Location")
	return fig

# Run the app
if __name__ == '__main__':
	app.run(debug=True)

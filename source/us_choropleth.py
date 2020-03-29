'''
US Choropleth Class
-------------------
This class will contain the ability to creath a choropleth map of the US.
'''

import plotly.graph_objects as go
import pandas as pd

class USChoropleth:
	def __init__(self, df):
		'''Initializes US Choropleth Map '''
		self.data = df

	def create_map(self, df):
		'''Sends in information from the states into the Choropleth'''
		
		fig = go.Figure(data=go.Choropleth(
		    locations=df['code'], # Spatial coordinates
		    z = df['total exports'].astype(float), # Data to be color-coded
		    locationmode = 'USA-states', # set of locations match entries in `locations`
		    colorscale = 'Reds',
		    colorbar_title = "Millions USD",
		))

		fig.update_layout(
		    title_text = '2011 US Agriculture Exports by State',
		    geo_scope='usa', # limite map scope to USA
		)

		fig.show()

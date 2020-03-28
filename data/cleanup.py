'''
Cleanup File
------------
This file will contain functionality to cleanup the .csv file to our particular
liking. Since we are only looking for United States locations, we can drop
all other data than that.
'''

import pandas as pd

def clean_country():
	'''Clean file to only contain United States location'''

	df = pd.read_csv(r'GlobalLandTemperaturesByState.csv')
	clean_df = df.loc[df['Country'] == 'United States']
	clean_df.to_csv('GlobalLandTemperaturesByState_Clean.csv')

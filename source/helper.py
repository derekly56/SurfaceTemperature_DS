'''
Helper File
-----------
This file will contain helper functions to help manage ingesting data from
the .csv file and then cleaning it up.
'''

import pandas as pd

united_states_code = {
	'Alabama' : 'AL', 'Alaska' : 'AK', 'Arizona' : 'AZ', 'Arkansas' : 'AR',
	'California' : 'CA', 'Colorado' : 'CO', 'Connecticut' : 'CT', 'Delaware' : 'DE',
	'Florida' : 'FL', 'Georgia' : 'GA', 'Hawaii' : 'HI', 'Idaho' : 'ID',
	'Illinois' : 'IL', 'Indiana' : 'IN', 'Iowa' : 'IA', 'Kansas' : 'KS',
	'Kentucky' : 'KY', 'Louisiana' : 'LA', 'Maine' : 'ME', 'Maryland' : 'MD',
	'Massachusetts' : 'MA', 'Michigan' : 'MI', 'Minnesota' : 'MN', 'Mississippi' : 'MS',
	'Missouri' : 'MO', 'Montana' : 'MT', 'Nebraska' : 'NE', 'Nevada' : 'NV',
	'New Hampshire' : 'NH', 'New Jersey' : 'NJ', 'New Mexico' : 'NM', 'New York' : 'NY',
	'North Carolina' : 'NC', 'North Dakota' : 'ND', 'Ohio' : 'OH', 'Oklahoma' : 'OK',
	'Oregon' : 'OR', 'Pennsylvania' : 'PA', 'Rhode Island' : 'RI', 'South Carolina' : 'SC',
	'South Dakota' : 'SD', 'Tennessee' : 'TN', 'Texas' : 'TX', 'Utah' : 'UT',
	'Vermont' : 'VT', 'Virginia' : 'VA', 'Washington' : 'WA', 'West Virginia' : 'WV',
	'Wisconsin' : 'WI', 'Wyoming' : 'WY'
}

def load_file(path):
	'''Grabs the data from the file and loads in Df'''
	cols = ['ID', 'Date', 'AverageTemperature', 'AverageTemperatureUncertainty', 'State', 'Country']
	df = pd.read_csv(path, header=0, names=cols)

	return df

def convert_states_to_abbr(df):
	'''Iterates over dataframe and change states to Abbreviation'''
	df = df.replace({'State' : self.states})

	return df

def clean_dataframe(df):
	'''Cleans the df by dropping Nan values and only using specific range of dates'''
	df.dropna()
	mask = (df['Date'] > '1900-01-01') & (df['Date'] <= '2013-08-01')
	df = df.loc[mask]
	print(df.head())
	
	return df

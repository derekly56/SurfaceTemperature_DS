'''
'''

import pandas as pd
import os
from source.us_choropleth import USChoropleth
from source.helper import load_file, convert_states_to_abbr, clean_dataframe

def main():
	# Path of .csv
	path = os.getcwd() + '/data/GlobalLandTemperaturesByState_Clean.csv'

	# Load and clean data into correct format
	temperature_df = load_file(path)
	converted_df = convert_states_to_abbr(temperature_df)
	clean_df = clean_dataframe(converted_df)

	


if __name__ == '__main__':
	main()

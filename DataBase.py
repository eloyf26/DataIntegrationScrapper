import pandas as pd
import sqlite3

def GetPandasDataFrame():
	# Define filepath
	filepath = 'DataBase.xlsx'

	# Load Excel file using Pandas
	f = pd.ExcelFile(filepath)

	# Define an empty list to store individual DataFrames
	list_of_dfs = []

	# Iterate through each worksheet
	for sheet in f.sheet_names:
		
		# Parse data from each worksheet as a Pandas DataFrame
		df = f.parse(sheet)

		# And append it to the list
		list_of_dfs.append(df)

	return list_of_dfs

def DfToSql(list_of_dfs):
	conn = sqlite3.connect('test.db')
	c = conn.cursor()

	c.execute('CREATE TABLE IF NOT EXISTS movies (title text, release_date number, rating number, duration text, poster string, genre strin, summary string, score string, director string, cast string, trailer string)')
	conn.commit()
	list_of_dfs[0].to_sql('movies', conn, if_exists='replace', index = False)

	c.execute('CREATE TABLE IF NOT EXISTS museums (name text, image text, description text, address text, publiv_transport text, visit_hours text, price number)')
	conn.commit()
	list_of_dfs[1].to_sql('museums', conn, if_exists='replace', index = False)

	c.execute('CREATE TABLE IF NOT EXISTS Tvguia (date text, timing text, channel text, program_name text)')
	conn.commit()
	list_of_dfs[0].to_sql('Tvguia', conn, if_exists='replace', index = False)

	c.execute('CREATE TABLE IF NOT EXISTS twitter (filmus_name text, tweet text, urls text, likes number, rts number)')
	conn.commit()
	list_of_dfs[0].to_sql('twitter', conn, if_exists='replace', index = False)

	c.execute('CREATE TABLE IF NOT EXISTS weather (location text, date text, hours text, max_min_temperature text, temperature number,image_url text, rain number)')
	conn.commit()
	list_of_dfs[0].to_sql('weather', conn, if_exists='replace', index = False)

	c.execute('CREATE TABLE IF NOT EXISTS cinema (date text, cinema text, films text, time text)')
	conn.commit()
	list_of_dfs[0].to_sql('cinema', conn, if_exists='replace', index = False)

	c.execute('CREATE TABLE IF NOT EXISTS cultural_places (place_name text, type text, latitude number, longitude number, location string, telephone_number number)')
	conn.commit()
	list_of_dfs[0].to_sql('cultural_places', conn, if_exists='replace', index = False)


DfToSql(GetPandasDataFrame())
import pandas as pd
import sqlite3
import os

def GetPandasDataFrame(filepath):

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

	if (os.path.exists(r"C:\Users\eloyfernandez\Documents\Uni\integracion de datos\DataIntegrationScrapper\DataBase.db")):
		os.remove(r"C:\Users\eloyfernandez\Documents\Uni\integracion de datos\DataIntegrationScrapper\DataBase.db")

	conn = sqlite3.connect('DataBase.db')
	c = conn.cursor()
	# c.execute('CREATE TABLE IF NOT EXISTS movies (title text NOT NULL PRIMARY KEY, release_date text, rating number, duration text, poster string, genre string, summary string, score string, director string, cast string, trailer string);')
	# conn.commit()
	# list_of_dfs[0].to_sql('movies', conn, if_exists='append', index = False)

	c.execute('CREATE TABLE IF NOT EXISTS museums (name text NOT NULL PRIMARY KEY, interesting_fact text, image text, category text, description text, address text, visiting_hours text);')
	conn.commit()
	list_of_dfs[0].to_sql('museums', conn, if_exists='append', index = False)

	c.execute('CREATE TABLE IF NOT EXISTS tvguia (date text NOT NULL, timing text NOT NULL, channel text NOT NULL, program_name text NOT NULL, PRIMARY KEY(date, timing, channel, program_name));')
	conn.commit()
	list_of_dfs[1].to_sql('tvguia', conn, if_exists='append', index = False)

	# c.execute('CREATE TABLE IF NOT EXISTS twitter (filmus_name text NOT NULL, user_id text , tweet text NOT NULL, likes number, retweets number, PRIMARY KEY(filmus_name, tweet));')
	# conn.commit()
	# list_of_dfs[3].to_sql('twitter', conn, if_exists='append', index = False)

	c.execute('CREATE TABLE IF NOT EXISTS weather (location text NOT NULL, date text NOT NULL, max_min_temperature text, hour text NOT NULL, temperature number, image_url text, rain number, PRIMARY KEY(location, date, hour));')
	conn.commit()
	list_of_dfs[2].to_sql('weather', conn, if_exists='append', index = False)

	c.execute('CREATE TABLE IF NOT EXISTS cinemas (date text NOT NULL, cinema text NOT NULL, films text NOT NULL, time text NOT NULL, PRIMARY KEY(date, cinema, films, time));')
	conn.commit()
	list_of_dfs[3].to_sql('cinemas', conn, if_exists='append', index = False)

	c.execute('CREATE TABLE IF NOT EXISTS cultural_places (place_name text NOT NULL PRIMARY KEY, type text, latitude number, longitude number, location string, telephone_number text);')
	conn.commit()
	list_of_dfs[4].to_sql('cultural_places', conn, if_exists='append', index = False)


# DfToSql(GetPandasDataFrame())

# CREATE TABLE IF NOT EXISTS musi (name TEXT, image TEXT, description TEXT, address TEXT, publiv_transport TEXT, visit_hours TEXT, price FLOAT)
# CREATE TABLE IF NOT EXISTS Tvg (date text, timing text, channel text, program_name text)
# CREATE TABLE IF NOT EXISTS cultural (place_name text NOT NULL PRIMARY KEY, type text, latitude number, longitude number, location string, telephone_number number UNIQUE)
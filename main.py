from movieIMDb import get_movies
from weather import get_weather
from cinemas import get_cinemas
from twitter import get_tweets
from Selenium_TVGuia import Selenium_bot

TvGuiaInfo = Selenium_bot()
print(TvGuiaInfo)
print("\n")

movies_url = "https://www.imdb.com/showtimes/location?ref_=sh_lc"
movies = get_movies(movies_url)
print(movies)
print("\n")

cinemas_url = "https://www.imdb.com/showtimes/"
cinemas = get_cinemas(cinemas_url)
print(cinemas)
print("\n")

weather_url = "https://www.aemet.es/es/eltiempo/prediccion/municipios?p=28&w=t"
weather = get_weather(weather_url)
print(weather)
print("\n")

tweets = get_tweets(movies)
print(tweets)







# museums_url = 


# tvguia_url = 
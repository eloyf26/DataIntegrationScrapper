from movieIMDb import get_movies
from weather import get_weather
from cinemas import get_cinemas
from twitter import get_tweets
from Selenium_TVGuia import Selenium_bot
import xlsxwriter


def Excel_Movies(movies,workbook):
    W_Movies = workbook.add_worksheet("Movies")
    row = 1
    W_Movies.write(0, 0, "Title") #Title
    W_Movies.write(0, 1, "Release Date") #Release date
    W_Movies.write(0, 2, "Rating") #Rating
    W_Movies.write(0, 3, "Duration") #Duration
    W_Movies.write(0, 4, "Poster") #Poster
    W_Movies.write(0, 5, "Genre") #Genre
    W_Movies.write(0, 6, "Summary") #Summary
    W_Movies.write(0, 7, "Score") #Score
    W_Movies.write(0, 8, "Director") #Director
    W_Movies.write(0, 9, "Cast") #Cast
    W_Movies.write(0, 10, "Trailer") #Trailer
    for movie in movies:
        actors = ""

        #Fill the first 8 columns
        for i in range(0,9):
            W_Movies.write(row, i, movie[i]) #Title
        
        try:
            for actor in movie[9]:
                actors += " " + actor
        except:
            actors = ""
        W_Movies.write(row, 9, actors) #Cast
        W_Movies.write(row, 10, movie[10]) #Trailer
        row += 1

def Excel_Tvguia(TvGuiaInfo,workbook):
    W_Tvguia = workbook.add_worksheet("Tvguia")
    #Set initial columns
    W_Tvguia.write(0, 0, "date") #Title
    W_Tvguia.write(0, 1, "timing") #Release date
    W_Tvguia.write(0, 2, "channel") #Rating
    W_Tvguia.write(0, 3, "program_name") #Duration
    row = 1
    #extract Days 
    for a in TvGuiaInfo:
        day = a[0]
        # a=[day n , [    [  [ channel , [[program1, time] [program2, time] [program3, time] ... ]]    [] [] ...(121 channels) ]    []    []   ... (8 time periods)  ]     ]    
        # each time period arrat
        for b in a[1]:
            #each channel in this time period
            for c in b:
                channel = c[0]
                #each program array in this channel
                for d in c[1]:
                    program_name = d[0]
                    program_time = d[1]
                    W_Tvguia.write(row,0,day)
                    W_Tvguia.write(row,1,program_time)
                    W_Tvguia.write(row,2,channel)
                    W_Tvguia.write(row,3,program_name)
                    row += 1
    return
 
workbook = xlsxwriter.Workbook('Database.xlsx')

TvGuiaInfo = Selenium_bot()
Excel_Tvguia(TvGuiaInfo,workbook)

movies_url = "https://www.imdb.com/showtimes/location?ref_=sh_lc"
movies = get_movies(movies_url)
Excel_Movies(movies,workbook)

#W_Cinemas = workbook.add_worksheet("Cinemas")
#cinemas_url = "https://www.imdb.com/showtimes/"
#cinemas = get_cinemas(cinemas_url)
#print(cinemas)
#print("\n")

#W_Weather = workbook.add_worksheet("Weather")
#weather_url = "https://www.aemet.es/es/eltiempo/prediccion/municipios?p=28&w=t"
#weather = get_weather(weather_url)
#print(weather)
#print("\n")

#W_Tweeter = workbook.add_worksheet("Tweets")
#tweets = get_tweets(movies)
#print(tweets)

workbook.close()






# museums_url = 


# tvguia_url = 
from movieIMDb import get_movies
from weather import get_weather
from cinemas import get_cinemas
from twitter import get_tweets
from museum import get_museums
from Selenium_TVGuia import Selenium_bot
import xlsxwriter
import openpyxl as xl


def Excel_Movies(movies,workbook):
    W_Movies = workbook.add_worksheet("movies")
    W_Movies.write(0, 0, "title") #Title
    W_Movies.write(0, 1, "release_date") #Release date
    W_Movies.write(0, 2, "rating") #Rating
    W_Movies.write(0, 3, "duration") #Duration
    W_Movies.write(0, 4, "poster") #Poster
    W_Movies.write(0, 5, "genre") #Genre
    W_Movies.write(0, 6, "summary") #Summary
    W_Movies.write(0, 7, "score") #Score
    W_Movies.write(0, 8, "director") #Director
    W_Movies.write(0, 9, "cast") #Cast
    W_Movies.write(0, 10, "trailer") #Trailer
    row = 1
    for movie in movies:
        actors = ""

        #Fill the first 8 columns
        for i in range(0,9):
            W_Movies.write(row, i, movie[i])
        
        try:
            for actor in movie[9]:
                actors += " " + actor
        except:
            actors = ""
        W_Movies.write(row, 9, actors) #Cast
        W_Movies.write(row, 10, movie[10]) #Trailer
        row += 1
    return


def Excel_Tvguia(TvGuiaInfo,workbook):
    W_Tvguia = workbook.add_worksheet("tvguia")
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


def Excel_Museums(museumsInfo, workbook):
    W_Museums = workbook.add_worksheet("museums")
    W_Museums.write(0, 0, "name") #Museum name
    W_Museums.write(0, 1, "interesting_fact") #Museum best known painting
    W_Museums.write(0, 2, "image") #Museum image
    W_Museums.write(0, 3, "category") #Museum category
    W_Museums.write(0, 4, "description") #Museum description
    W_Museums.write(0, 5, "address") #Museum address
    W_Museums.write(0, 6, "visiting_hours") #Museum hours
    #W_Museums.write(0, 7, "telephone") #Contact information -> We get it from Excel file
    row = 1

    for museum in museumsInfo:
        col = 0
        last = len(museum) - 1
        for info in museum:
            if info != museum[last]:
                W_Museums.write(row, col, info)
                col += 1
        row += 1
    return


def Excel_Weather(weather, workbook):
    W_Weather = workbook.add_worksheet("weather")
    W_Weather.write(0, 0, "location") #Location name
    W_Weather.write(0, 1, "date") #Day
    W_Weather.write(0, 2, "max_min_temperature") #Max/Min temperature
    W_Weather.write(0, 3, "hour") #Hour
    W_Weather.write(0, 4, "temperature") #Temperature (ºC)
    W_Weather.write(0, 5, "image_url") #Image
    W_Weather.write(0, 6, "rain") #Rain (%)
    row = 1

    for location in weather:
        loc = location[0] #Location
        d = location [1] #Date
        temp = location[2] #max_min_temperature
        arr = location[3]
        i = 0
        #hour, temperature, image, rain
        for info in arr:
            col = 3
            for extra in info:
                W_Weather.write(row, 0, loc)
                W_Weather.write(row, 1, d)
                W_Weather.write(row, 2, temp)
                W_Weather.write(row, col, extra)
                col += 1
            row += 1
    return


def Excel_Cinemas(cinemas,workbook):
    W_Cinemas = workbook.add_worksheet("cinemas")

    W_Cinemas.write(0, 0, "date") #Date
    W_Cinemas.write(0, 1, "cinema") #Cinema name
    W_Cinemas.write(0, 2, "films") #Film name
    W_Cinemas.write(0, 3, "time") #Film schedule time

    row = 1

    for cine in cinemas:
        date = cine[0]
        cinema_name = cine[1]
        film_name = cine[2]
        for time in cine[3]:
            W_Cinemas.write(row,0,date)
            W_Cinemas.write(row,1,cinema_name)
            W_Cinemas.write(row,2,film_name)
            W_Cinemas.write(row,3,time)

            row += 1

    return

def Excel_Twitter(TwitterInfo,workbook):
    W_Twitter = workbook.add_worksheet("twitter")
    #Set initial columns
    W_Twitter.write(0, 0, "filmus_name")
    W_Twitter.write(0, 1, "userID")
    W_Twitter.write(0, 2, "tweer")
    W_Twitter.write(0, 3, "likes")
    W_Twitter.write(0, 4, "retweets")
    row = 1

    for all_tweets in TwitterInfo:
        name = all_tweets[0]
        for tweet in all_tweets[1]:
            if tweet != "o":
                W_Twitter.write(row, 0, name) #Film/museum name
                W_Twitter.write(row, 1, str(tweet[0])) #User ID
                W_Twitter.write(row, 2, tweet[1]) #Text 
                W_Twitter.write(row, 3, tweet[2]) #Likes
                W_Twitter.write(row, 4, tweet[3]) #Retweets
                row += 1
    return


def Excel_Cultural_Places(workbook):
    # opening the source excel file
    filename ="cultural_places.xlsx"
    wb1 = xl.load_workbook(filename)
    ws1 = wb1.worksheets[0]
      
    # opening the destination excel file 
    W_Places = workbook.add_worksheet("cultural_places")
      
    # calculate total number of rows and 
    # columns in source excel file
    mr = ws1.max_row
    mc = ws1.max_column
      
    # copying the cell values from source 
    # excel file to destination excel file
    for i in range (1, mr + 1):
        for j in range (1, mc + 1):
            # reading cell value from source excel file
            c = ws1.cell(row = i, column = j).value
            # print (c)
      
            # writing the read value to destination excel file
            W_Places.write(i-1, j-1, c)

    return


workbook = xlsxwriter.Workbook('Database.xlsx')

print("Obtaining movies info.............")
movies_url = "https://www.imdb.com/showtimes/location?ref_=sh_lc"
movies = get_movies(movies_url)
print("Creating movies Excel.............")
Excel_Movies(movies,workbook)

print("Obtaining museums info.............")
museums_url = "https://es.hoteles.com/go/espana/mejores-museos-de-madrid"
museumsInfo = get_museums(museums_url)
print("Creating museums Excel.............")
Excel_Museums(museumsInfo, workbook)

print("Obtaining TVGuia info.............")
TvGuiaInfo = Selenium_bot()
print("Creating TVGuia Excel.............")
Excel_Tvguia(TvGuiaInfo,workbook)

print("Obtaining Twitter info...........")
tweets = get_tweets(movies)
print("Creating Twitter sheet...........")
Excel_Twitter(tweets, workbook)

print("Obtaining weather info.............")
weather_url = "https://www.aemet.es/es/eltiempo/prediccion/municipios?p=28&w=t"
weather = get_weather(weather_url)
print("Creating weather Excel.............")
Excel_Weather(weather, workbook)

print("Obtaining cinemas info.............")
cinemas_url = "https://www.imdb.com/showtimes/ES/28912/"
cinemas = get_cinemas(cinemas_url)
print("Creating cinemas Excel.............")
Excel_Cinemas(cinemas,workbook)

print ("Obtaining cultural places info and creating excel.............")
Excel_Cultural_Places(workbook)

workbook.close()
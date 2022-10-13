from bs4 import BeautifulSoup
import requests

# url = "https://www.aemet.es/es/eltiempo/prediccion/municipios?p=28&w=t"

def get_weather (url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    all_locations = soup.find_all('tr', class_ = 'localidades')

    all_info = []
    # print(all_locations)

    for locations in all_locations:

        loc = locations.find_all('td')
        # print(locations)
        
        for l in loc:

            location_info = []

            locurl = "https://www.aemet.es" + l.a['href']
            page = requests.get(locurl)
            soup = BeautifulSoup(page.content, 'html.parser')

            #Location
            location = l.text.strip()
            location_info.append(location)
            # print(f'Location: {location}')

            #Day
            try:
                day = soup.find_all('th', class_ = 'borde_izq_dcha_fecha')[0].text.strip()
                location_info.append(day)
                # print(f'    Day: {day}')
            except:
                day = None
                # print(day)
                location_info.append(day)

            #Maximum and minimum temperatures
            try:
                maxmin_temp = soup.find('td', class_ = 'alinear_texto_centro no_wrap comunes').text.strip().replace('\xa0','')
                # print(f'    Max/Min: {maxmin_temp}')
                location_info.append(maxmin_temp)
            except:
                maxmin_temp = None
                # print(maxmin_temp)
                location_info.append(maxmin_temp)

            hours = soup.find_all('th', class_ = 'borde_izq_dcha_estado_cielo no_wrap')
            rain = soup.find_all('td', class_ = 'nocomunes')
                
            for j in range (4):
                hours_info = []

                #Hours
                try:
                    h = hours[j].find('div', class_ = 'fuente09em').text.strip().replace('\xa0',' ')
                    # print(f'        Hours: {h}')
                    hours_info.append(h)
                except:
                    h = None
                    # print(hours)
                    hours_info.append(h)
                    
                 #Temperature & Image
                try:
                    temp = hours[j].find('div', class_ = 'no_wrap').text.strip()
                    img = "https://www.aemet.es" + hours[j].find('img')['src']
                    # print(f'            Temperature: {temp}')
                    # print(f'            Image: {img}')
                    hours_info.append(temp)
                    hours_info.append(img)
                except:
                    temp = None
                    # print(temp)
                    hours_info.append(temp)
                    hours_info.append(temp)

                #Rain
                try:
                    r = rain[j].text.strip()
                    # print(f'            Rain: {r}')
                    hours_info.append(r)
                except:
                    r = None
                    # print(r)
                    hours_info.append(r)

                location_info.append(hours_info)
            all_info.append(location_info)
    return all_info
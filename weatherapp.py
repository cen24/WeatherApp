from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests

# Back end: using API to retrieve weather data.
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


#Json file to
def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        #(City, Country, temp_celsius, temp_fahrenheit, icon, weather)
        city = json['name']
        country = json['sys']['country']
        temp_kelv = json['main']['temp']
        temp_celsius = (temp_kelv -273.15)
        temp_fahrenheit = (temp_kelv -273.15) * 9 / 5 +32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city,country,temp_celsius,temp_fahrenheit,icon
                 ,weather)
        return final
    else:
        return None


# Retrieve data into our local app *Weather by 32*

def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_label['text'] = '{}, {}'.format(weather[0], weather[1])
        image['bitmap'] = 'weather_icons/{}.png'.format(weather[4])
        temperature_label['text'] = '{:.0f}°C, {:.0f}°F'.format(weather[2], weather[3])
        weather_label['text'] = weather[5]
    else:
        messagebox.showerror('Error','City not found{}'.format(city))

app = Tk()
app.title('WeatherApp by Chinedu32')
app.geometry('700x350')

city_text = StringVar()
city_entry = Entry(app,textvariable=city_text)
city_entry.pack()
# '.pack' to display on UI.

search_button = Button(app, text='Search city', width=12, command=search, font=('bold', 15))
search_button.pack()

location_label = Label(app, text='', font=('bold', 20))
location_label.pack()

image = Label(app, bitmap='')
image.pack()

temperature_label = Label(app, text='')
temperature_label.pack()

weather_label = Label(app, text='')
weather_label.pack()

app.mainloop()



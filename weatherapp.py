from tkinter import *
from configparser import ConfigParser
import requests

# To get API
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        print(result.content)
    else:
        return None
get_weather('London')

def search():
    pass

app = Tk()
app.title('Weather by 32')
app.geometry('700x350')

city_text = StringVar()
city_entry = Entry(app,textvariable=city_text)
city_entry.pack()
# '.pack' to display on UI.

search_button= Button(app, text='', width=12, command=search)
search_button.pack()

location_label= Label(app, text='', font=('bold', 20))
location_label.pack()

image = Label(app, bitmap='')
image.pack()

temperature_label= Label(app, text='')
temperature_label.pack()

weather_label= Label(app, text='')
weather_label.pack()

app.mainloop()



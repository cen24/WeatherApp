from tkinter import *

def search():
    pass

app = Tk()
app.title('Weather by 32')
app.geometry('700x350')

city_text = StringVar()
city_entry = Entry(app,textvariable=city_text)
city_entry.pack()

search_button= Button(app, text='Search Weather', width=12, command=search)
search_button.pack()

location_label= Label(app, text='Location', font=('bold', 20))
location_label.pack()

image = Label(app, bitmap='')
image.pack()

temperature_label= Label(app, text='temperature')
temperature_label.pack()

weather_label= Label(app, text='weather')
weather_label.pack()

app.mainloop()



from tkinter import *

app = Tk()
app.title('Weather by 32')
app.geometry('700x350')

city_text = StringVar()
city_entry = Entry(app,textvariable=city_text)
city_entry.pack()


app.mainloop()



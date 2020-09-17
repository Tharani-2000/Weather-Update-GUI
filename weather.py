import requests
from tkinter import *
import sys


def getinfo():
    url = "http://api.openweathermap.org/data/2.5/weather?q="
    key = "b082f088b5078dfd739c610a48a5bc5c"
    cityname = et.get()

    data = requests.get(url + cityname + "&appid=" + key).json()

    if data['cod'] != 404:
        lat = data['coord']['lat']
        long = data['coord']['lon']
        temp = data['main']['temp']
        temp = float(temp) - 273.15
        wind = data['wind']['speed']
    else:
        lat = long = "City is not found"
        temp = wind = ""

    LAT.configure(text="Lat:    " + str(lat))
    LONG.configure(text="Lon:    " + str(long))
    Temperature.configure(text="Temperature (~c):    " + str(temp))
    Wind_speed.configure(text="Wind Speed:       " + str(wind))


def Exit():
    window.destroy()
    sys.exit()


window = Tk()
window.title("Weather Information")
window.geometry("450x300")


Title = Label(window, text="Weather", font=("Arial Bold", 14))
l1 = Label(window, text="Enter the Adress")
bt = Button(window, text="Enter", command=getinfo)
btn = Button(window, text="Quit", command=Exit)

et = Entry(window, width=40)
LAT = Label(window, text="Lat:    ")
LONG = Label(window, text="Lon:    ")
Temperature = Label(window, text="Temoerature (~C):    ")
Wind_speed = Label(window, text="Wind_speed:    ")


Title.grid(row=0, column=1)
l1.grid(row=2, column=0)
et.grid(row=2, column=1)
bt.grid(row=4, column=1)
btn.grid(row=5, column=1)
LAT.grid(row=7, column=0)
LONG.grid(row=8, column=0)
Temperature.grid(row=7, column=1)
Wind_speed.grid(row=8, column=1)

window.mainloop()
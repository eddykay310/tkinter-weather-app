import tkinter as tk
from PIL import Image, ImageTk
import requests
from tkinter import font
from format_response import format_response
import config

root = tk.Tk()
height = 600
width = 600

root.title("Weather App")
root.geometry('600x600')
root.iconbitmap("weather_image.ico")

def get_weather(city):
    try:
        # print(city)
        # units ='imperial'
        # url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{units}&appid={apikey}"
        params = {'appid':apikey,'q':city,'units':'imperial'}
        url = "https://api.openweathermap.org/data/2.5/weather"
        response = requests.get(url,params=params)
        weather = response.json()
        label['text'] = format_response(weather)
    except:
        label['text']= "Check your internet connection"
    return label

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    bgimage_label.config(image = photo)
    bgimage_label.image = photo 

# canvas = tk.Canvas(root,height=height,width=width,bg='black')
# canvas.pack()

image = Image.open('background_image.gif')
copy_of_image = image.copy()
bgimage = tk.PhotoImage(file='background_image.gif')
bgimage_label = tk.Label(root,image=bgimage)
# bgimage_label.place(relwidth=1,relheight=1)

bgimage_label.bind('<Configure>', resize_image)
bgimage_label.pack(fill='both', expand = True)

############ Alternative for rendering image
# image = Image.open('background_image.gif')
# photo = ImageTk.PhotoImage(image)
# label = tk.Label(image=photo)
# label.place(relwidth=1,relheight=1)


frame = tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry = tk.Entry(frame,font=('Courier',12))
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame,text='Get Weather',font=('Courier',12),command=lambda: get_weather(entry.get()))
button.place(relx=0.7,relwidth=0.3,relheight=1)


bottom_frame = tk.Frame(root,bg='#80c1ff',bd=10)
bottom_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label = tk.Label(bottom_frame,font=('Courier',12),anchor='nw',justify='left',)
label.place(relwidth=1,relheight=1)

root.mainloop()
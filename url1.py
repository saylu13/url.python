# URL Shortener Project using Python Language


import tkinter
import pyshorteners

def shorten():
    shortener = pyshorteners.Shortener()
    
    text = input1_url.get()
    
    short_url = shortener.tinyurl.short(text)
    
    input2_shortened_url.insert(0 , short_url)
    

rootWindow = tkinter.Tk()  # Parent Window

rootWindow.title("URL Shortener Project")

rootWindow.geometry("1200x700")

rootWindow.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333')

msg = tkinter.Label(frame , text = "URL Shortener using Python" , fg='#FF3399' , bg='#333333' , font = ('Arial',25))
msg.grid(row = 0 , column = 0 , columnspan = 2 , sticky = 'news' , pady = 40)


label1_message = tkinter.Label(frame , text = "Paste URL" , fg='white' , bg='#333333' , font = ('Arial',15))
label1_message.grid(row = 1 , column = 0)

input1_url = tkinter.Entry(frame , width = 100 , font = ('Arial',15))
input1_url.grid(row = 1 , column = 1 , pady = 20)


label2_message = tkinter.Label(frame , text = "Shortened URL" , fg='white' , bg='#333333' , font = ('Arial',15))
label2_message.grid(row = 2 , column = 0)

input2_shortened_url = tkinter.Entry(frame , width = 100 , font = ('Arial',15))
input2_shortened_url.grid(row = 2 , column = 1  , pady = 20)


shortener_button = tkinter.Button(frame , text = "Shorten URL" , command=shorten , fg='white' , bg='#FF3399'  , font = ('Arial',15))
shortener_button.grid(row = 3 , column = 0 , columnspan=2 , pady = 30)


frame.pack()

rootWindow.mainloop()
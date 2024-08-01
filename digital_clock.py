#import liberary
from tkinter import Label, Tk 
import time

#creating the main Window
app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
app_window.resizable(1,1)

#setting up label apperence
text_font= ("Boulder", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25

#creating the Label
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

#Defining the clock function
def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) #this updates the label text to show the current time
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
import opencage
from opencage.geocoder import OpenCageGeocode
import folium


splash = Tk()
splash.title ('GodardGPT')
splash.geometry ('400x400')
splash.resizable (0,0)
splash.configure (background = 'red')
spl_lab = Label (splash, text = 'GodARD Devos \n GodNumberTracker', bg = 'yellow', fg = 'blue', font = ('vendana', 20, 'bold'))
spl_lab.pack (pady = 150)

def numberGodard():
        splash.destroy()
        numtr = tk.Tk()
        numtr.geometry ('1200x500')
        numtr.title ("Godard Number Tracker")
        numtr.configure (background = '#CD3333')
        numtr.resizable (0,0)
        numtr.minsize (width = 950, height = 600)

        def ClearBtn():
            noask.delete(0,END)
            labelq.destroy()
            labelqq.destroy()
            

        def numbercont ():
            global notrack
            global labelq
            global labelqq
            global api_key
            global geocoder

            notrack = str(noask.get())
            numtrack = phonenumbers.parse(notrack)
            loctrack = geocoder.description_for_number(numtrack , "en")
            labelq = Label(numtr,text=f'Number Is From {loctrack}',bg='black',fg='white',font=('vendana',30,'bold'))
            labelq.place(x = 430, y = 300)
            
            simno = phonenumbers.parse(notrack)
            simcom = carrier.name_for_number(simno , "en")
            labelqq = Label(numtr,text=f'It was / is a {simcom} SIM when bought',bg='white',fg='black',font=('vendana',30,'bold'))
            labelqq.place(x = 290, y = 350)

            api_key = "#"
            geocoder = OpenCageGeocode(api_key)
            query = str(loctrack)
            res = geocoder.geocode(query)
            lati = res[0]['geometry']['lat']
            long = res[0]['geometry']['lng']
            labelqqq = Label(numtr,text=f'location = Latitude {lati} ; Longitude {long}',bg='black',fg='white',font=('vendana',20,'bold'))
            labelqqq.place(x = 300, y = 420)
            
            map = folium.Map(location = [lati,long], zoom_start = 8)
            folium.Marker([lati,long], popup = loctrack).add_to(map)
            map.save('GodKnows.html')

            labelqqqq = Label(numtr,text=f'Google Map Of Particular Location Saved As "GodKnows.html" In Your Locals.',bg='white',fg='black',font=('vendana',20,'bold'))
            labelqqqq.place(x = 150, y = 460)            
              
        # Labels
        
        labelh = Label(numtr,text='Enter The Number Here',bg='green',fg='#CD3333',font=('vendana',40,'bold'))
        labelh.place(x = 330, y = 50)

        #Entry
        
        noask = Entry (numtr, width = 45, bg = 'pink', fg = 'red', borderwidth = 4,
        font = ('vendana', 20,'italic'))
        noask.insert (0,"Enter Number eg. (+88 9999999999) ...")
        noask.place(x= 290, y = 130)
        
        # Buttons
                
        det = Button (numtr, width=10, height=1,text='Details',bg='brown', fg ='pink',command=numbercont,font=('vendana',20,'bold'))
        det.place(x = 300, y = 200)
        
        clear = Button (numtr, width=10, height=1,text='Clear',bg='brown', fg ='pink',command=ClearBtn,font=('vendana',20,'bold'))
        clear.place(x = 650, y = 200)        
        
# spalsh screen timer

splash.after ( 2500, numberGodard)

# run app

mainloop()

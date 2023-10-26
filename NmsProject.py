import tkinter
from pythonping import ping
import os
from numpy import loadtxt
from tkinter import *
from tkinter import filedialog as fd
import customtkinter

#Create main window for app
mainWindow = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
canvas = Canvas()
IPlabels = []
latencyLabels = []
statusLabels = []
myList = []

#Create File Select window
def fileSelectWindow():
    #define accepted file types
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    #select file
    file = fd.askopenfile(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    with file as file:
        ipList=file.read()
        ipList= ipList.splitlines()

        for ip in ipList:
            #creates list to store ping ouput
            response = os.popen(f"ping -n 1 {ip} ").read()
            myList.append(response)
            print(response)

    for x in myList:
        ip = x[9:17]
        y = myList.index(x)
        IPlabels.append(customtkinter.CTkLabel(frame, text=ip))
        IPlabels[y].place(x=45, y=50+(y*30))
    for x in myList:
        latency = x[75:79]
        y=myList.index(x)
        latencyLabels.append(customtkinter.CTkLabel(frame, text=latency))
        latencyLabels[y].place(x=215, y=50 + (y * 30))
    for x in myList:
        if("Request timed out." or "unreachable") in x:
            status = "Down"
            y = myList.index(x)
            statusLabels.append(customtkinter.CTkLabel(frame, text=status))
            statusLabels[y].place(x=320, y=50 + (y * 30))
        else:
            status = "Up"
            y = myList.index(x)
            statusLabels.append(customtkinter.CTkLabel(frame, text=status))
            statusLabels[y].place(x=320, y=50 + (y * 30))



#Set window width and height
mainWindow.geometry('500x500')
frame = customtkinter.CTkFrame(master = mainWindow, width = 450, height = 350, border_color="grey")
frame.pack(padx=50, pady=50)

#Create buttons
selectFile = customtkinter.CTkButton(mainWindow, text='Select File', font=("Inter", 10), command = fileSelectWindow)
#loadIp = customtkinter.CTkButton(mainWindow, text='load', font=("Inter", 10), command = loadIps)
title = customtkinter.CTkLabel(mainWindow, text = 'Network Monitoring Systems', corner_radius= 10, fg_color= 'grey', text_color='white')
ipLabel = customtkinter.CTkLabel(master = frame, text = 'IP', corner_radius= 10, fg_color= 'grey', text_color='white')
latencyLabel = customtkinter.CTkLabel(master= frame, text = 'Latency', corner_radius= 10, fg_color= 'grey', text_color='white')
statusLabel = customtkinter.CTkLabel(master=frame, text = 'Status', corner_radius= 10, fg_color= 'grey', text_color='white')

#Place Buttons in window
selectFile.place(x=175, y=450)
title.place(x=165, y=15)
ipLabel.place(x=50, y=15)
latencyLabel.place(x=200, y = 15)
statusLabel.place(x=300, y=15)




#runs app
mainWindow.mainloop()

import tkinter
from pythonping import ping
import os
from numpy import loadtxt
from tkinter import *
from tkinter import filedialog as fd
import customtkinter

#Create main window for app
mainWindow = customtkinter.CTk()
canvas = Canvas()

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
        myList=[]
        response = os.popen(f"ping -n 1 {ip} ").read()
        #if("Request timed out." or "unreachable") in response:

        #creates a lable to display IP and latency, im thinking we'll just cut the sections we want
        #out of the elements in the array and assign them to an individual label
        label = customtkinter.CTkLabel(mainWindow, text=response)
        label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        myList.append(response)

        #prints list so you can see what your working with
        #print(myList)
        Ip1 = myList[0]
        Ip2 = Ip1[0:10]
        print(Ip2)

        return myList

#def loadIps():
    #l = fileSelectWindow()
    #print(l)








#Set window width and height
mainWindow.geometry('500x500')

#Create buttons
selectFile = customtkinter.CTkButton(mainWindow, text='Select File', font=("Inter", 10), command = fileSelectWindow)
#loadIp = customtkinter.CTkButton(mainWindow, text='load', font=("Inter", 10), command = loadIps)

#Place Buttons in window
selectFile.place(x=200, y=450)
#loadIp.place(x=100, y=100)




#runs app
mainWindow.mainloop()

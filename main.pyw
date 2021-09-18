import os, time, webbrowser, requests
import filetype
import hanger
from tkinter import *
from tkinter import filedialog
from pathlib import Path

filename = str()

def Selectfile():
    global filename
    filename = filedialog.askopenfilename(initialdir = "./", title = "Select Image", filetypes = (("All Images","*jpg","*png"),("JPG","*.jpg"),("PNG","*.png"),("All files","*.*")))
    print("--Filename--" + filename)

    if filename == "": pass
    else: 
        Convertbutton["state"] = NORMAL
        Convertstatus.config(text = "STATUS: file selected, can convert now")
        Fileselected.config(text = "FILE: " + filename)
        Step1.config(fg = "#0F151D")
        Step2.config(fg = "#C96C00")

def Convert(filename):
    print("--file--" + filename)

    global img
    hangerClass = hanger.hanger(filename)
    img = hangerClass.template()
    img = hangerClass.insert()

    try:
        Convertstatus.config(text = "STATUS: Converted")
        Step2.config(fg = "#0F151D")
        Step3.config(fg = "#C96C00")
        Openlinkbutton["state"] = NORMAL
    except:
        Convertstatus.config(text = "ERROR CALLING ON HANGER")
        print("ERROR calling on hanger")

def OpenLink():
    print(img)
    webbrowser.open(img)
    Step2.config(fg = "#C96C00")
    Step2.config(fg = "#0F151D")
    Step3.config(fg = "#0F151D")
    Convertbutton["state"] = DISABLED
    Openlinkbutton["state"] = DISABLED

def Scriptbotlink():
    webbrowser.open("https://script-bot.netlify.com")

if __name__ == "__main__":

    root = Tk()

    root.title("Hanger")
    #root.geometry("525x250")
    root.resizable(0,0)
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='HangerLogo.png'))
    root.configure(background = '#0F151D')

    #Frames

    Tutorialandselectframe = Frame(root,bg = "#0F151D")
    Tutorialandselectframe.pack(anchor = W)

    Selectframe = Frame(Tutorialandselectframe,bg = "#0F151D")
    Selectframe.pack(side = RIGHT)

    Tutorialframe = Frame(Tutorialandselectframe,bg = "#0F151D")
    Tutorialframe.pack(side = LEFT)

    Infoframe = Frame(root,bg = "#0F151D")
    Infoframe.pack(side = BOTTOM)

    #Select frame stuff

    Selectfilebutton = Button(Selectframe, text = "Select File", command = Selectfile, height = 5, width = 10, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    Selectfilebutton.pack(anchor = W)

    Convertbutton = Button(Selectframe, text = "Convert", command = lambda: Convert(filename), height = 5, width = 10, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    Convertbutton.pack(anchor = W)

    Openlinkbutton = Button(Selectframe, text = "Open Link", command = lambda: OpenLink(), height = 5, width = 10, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    Openlinkbutton.pack(anchor = W)

    Convertbutton["state"] = DISABLED
    Openlinkbutton["state"] = DISABLED

    #Tutorial frame stuff

    Step1 = Label(Tutorialframe, text = "Step1: Select picture to use",bg = "#0F151D",fg = "#0F151D")
    Step1.pack(side = TOP,pady = 30)

    Step2 = Label(Tutorialframe, text = "Step2: Convert picture to template",bg = "#0F151D",fg = "#0F151D")
    Step2.pack(side = TOP,pady = 30)

    Step3 = Label(Tutorialframe, text = "Step3: Open link to template",bg = "#0F151D",fg = "#0F151D")
    Step3.pack(side = TOP,pady = 30)
    
    Step1.config(fg = "#C96C00")

    #Info frame stuff

    Convertstatus = Label(Infoframe, text = "STATUS: file not selected", bg = "#0F151D", fg = "#C96C00")
    Convertstatus.pack(side = TOP)

    Fileselected = Label(Infoframe, text = "FILE: none", bg = "#0F151D", fg = "#C96C00", wraplength = 250)
    Fileselected.pack(side = TOP)

    scriptbot = Button(Infoframe,justify = LEFT, command = Scriptbotlink, bg = '#2B2D31', fg='#C96C00', activebackground='#1E1B15', activeforeground='#066D9F')
    scriptbotphoto=PhotoImage(file="./logo.png")
    scriptbot.config(image=scriptbotphoto)
    scriptbot.pack(side = TOP)

    Version = Label(Infoframe, text = "Version: 1.1", bg = "#0F151D", fg = "#C96C00")
    Version.pack(side = TOP)

    root.mainloop()
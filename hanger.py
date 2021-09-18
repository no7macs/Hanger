from PIL import Image, ImageDraw
import requests, os, webbrowser, pathlib, json, shutil
import upload

def creation(basefilename,filetype,filedir,filename):
    template = Image.new("RGB", (585,559), "white")

    ending = str()

    if filetype == "png" or filetype == "PNG": ending = ".png"
    elif filetype == "jpg" or filetype == "JPG" or filetype == "JPEG" or filetype == "jpeg": ending = ".jpg"

    runningpath = (pathlib.Path(__file__).parent.absolute())
    shutil.copy(filename, runningpath)

    image = Image.open(basefilename)

    square = image.resize((128,128), Image.LANCZOS)

    tallrectangle = image.resize((64,128), Image.LANCZOS)

    longrectangle = image.resize((128,64), Image.LANCZOS)

    smallsquare = image.resize((64,64), Image.LANCZOS)

    paste(template,square,tallrectangle,longrectangle,smallsquare,filename,filetype,runningpath,basefilename)

def paste(template,square,tallrectangle,longrectangle,smallsquare,filename,filetype,runningpath,basefilename):

    #Font
    template.paste(square,(231,74,231 + 128,74 + 128))
    #Back
    template.paste(square,(427,74,427 + 128,74 + 128))
    #Right arm
    template.paste(tallrectangle,(165,74,165 + 64,74 + 128))
    #Left arm
    template.paste(tallrectangle,(361,74,361 + 64,74 + 128))
    #Torso top
    template.paste(longrectangle,(231,8,231 + 128,8 + 64))
    #Torso bottom
    template.paste(longrectangle,(231,204,231 + 128,204 + 64))

    #Left right arm
    template.paste(tallrectangle,(19,355,19 + 64,355 + 128))
    #Back right arm
    template.paste(tallrectangle,(85,355,85 + 64,355 + 128))
    #Right right arm
    template.paste(tallrectangle,(151,355,151 + 64,355 + 128))
    #Front right arm
    template.paste(tallrectangle,(217,355,217 + 64,355 + 128))
    #Up right arm
    template.paste(smallsquare,(217,289,217 + 64,289 + 64))
    #Down right arm
    template.paste(smallsquare,(217,485,217 + 64,485 + 64))


    #Front left arm
    template.paste(tallrectangle,(308,355,308 + 64,355 + 128))
    #Left left arm
    template.paste(tallrectangle,(374,355,374 + 64,355 + 128))
    #Back left arm
    template.paste(tallrectangle,(440,355,440 + 64,355 + 128))
    #Right left arm
    template.paste(tallrectangle,(506,355,506 + 64,355 + 128))
    #Up left arm
    template.paste(smallsquare,(308,289,308 + 64,289 + 64))
    #Down left arm
    template.paste(smallsquare,(308,485,308 + 64,485 + 64))

    if filetype == "png" or filetype == 'PNG': template.save("out" + ".png","PNG")
    elif filetype == "jpg" or filetype == "JPG" or filetype == "JPEG" or filetype == "jpeg": template.save("out" + ".jpg","JPEG")
    else: print("ERROR with saving completed template")

    try:
        global link
        link = upload.upload(filetype,runningpath,basefilename)
    except: 
        print("ERROR Calling on upload")

def openurl():
    webbrowser.open(link)

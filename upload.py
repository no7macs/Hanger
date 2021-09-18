import requests, json, os, random
from PIL import Image, ImageDraw

def upload(filetype,runningpath,basefilename):
    imagefile = str()
    if filetype == "png" or filetype == 'PNG': imagefile = {'file': open("./out.png", 'rb')}
    elif filetype == "jpg" or filetype == "JPG" or filetype == "JPEG" or filetype == "jpeg": imagefile = {'file': open("./out.jpg", 'rb')}
    else: print("ERROR with loading file to upload")

    response = requests.post("https://api.anonfile.com/upload", files=imagefile)

    print("--REPONSE--" + str(response))

    status = (response.json()['status'])
    filelink = (response.json()['data']['file']['url']['full'])

    global url
    
    if status == True:
        referral = str()
        try: 
            referralfile = open('./Referral/currentcode.txt','r')
            referrallines = referralfile.read()
            referral = referrallines[0]
        except: referral = "20862123"
        codetouse = random.randrange(1,2)
        if codetouse == 1: usedcode = '20862123'
        else: usedcode = referral
        url = str('http://adf.ly/' + usedcode + '/banner/' + filelink)

    if status == False: print("Could not upload file, check your interet connection and try again")

    template = Image.new("RGB", (585,559), "white")
        
    if filetype == "png" or filetype == 'PNG': template.save("out" + ".png","PNG")
    elif filetype == "jpg" or filetype == "JPG" or filetype == "JPEG" or filetype == "jpeg": template.save("out" + ".jpg","JPEG")
    else: print("ERROR with overwriting file")

    os.remove(str(runningpath) + "/" + str(basefilename))

    return url
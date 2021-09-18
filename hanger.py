from PIL import Image, ImageDraw
import filetype
import requests, os, pathlib, json, shutil
from PyAnonFile import pyanonfile

class hanger():
    def __init__(self, file):
        self.file = file
        self.fileType = filetype.guess(file).extension
        self.fileMIME = filetype.guess(file).mime
        self.fileBaseName = os.path.basename(file)
        self.fileName, self.fileEnding = (os.path.splitext(os.path.basename(self.fileBaseName)))
        self.fileDirName = os.path.dirname(file)

        self.runningPath = (pathlib.Path(__file__).parent.absolute())
        return
    
    def template(self):
        self.template = Image.new("RGB", (585,559), "white")
        return

    def insert(self):

        shutil.copy(self.file, self.runningPath)

        image = Image.open(self.fileBaseName)

        #resized imgages
        self.square = image.resize((128,128), Image.LANCZOS)
        self.tallrectangle = image.resize((64,128), Image.LANCZOS)
        self.longrectangle = image.resize((128,64), Image.LANCZOS)
        self.smallsquare = image.resize((64,64), Image.LANCZOS)

        #Font
        self.template.paste(self.square,(231,74,231 + 128,74 + 128))
        #Back
        self.template.paste(self.square,(427,74,427 + 128,74 + 128))
        #Right arm
        self.template.paste(self.tallrectangle,(165,74,165 + 64,74 + 128))
        #Left arm
        self.template.paste(self.tallrectangle,(361,74,361 + 64,74 + 128))
        #Torso top
        self.template.paste(self.longrectangle,(231,8,231 + 128,8 + 64))
        #Torso bottom
        self.template.paste(self.longrectangle,(231,204,231 + 128,204 + 64))

        #Left right arm
        self.template.paste(self.tallrectangle,(19,355,19 + 64,355 + 128))
        #Back right arm
        self.template.paste(self.tallrectangle,(85,355,85 + 64,355 + 128))
        #Right right arm
        self.template.paste(self.tallrectangle,(151,355,151 + 64,355 + 128))
        #Front right arm
        self.template.paste(self.tallrectangle,(217,355,217 + 64,355 + 128))
        #Up right arm
        self.template.paste(self.smallsquare,(217,289,217 + 64,289 + 64))
        #Down right arm
        self.template.paste(self.smallsquare,(217,485,217 + 64,485 + 64))


        #Front left arm
        self.template.paste(self.tallrectangle,(308,355,308 + 64,355 + 128))
        #Left left arm
        self.template.paste(self.tallrectangle,(374,355,374 + 64,355 + 128))
        #Back left arm
        self.template.paste(self.tallrectangle,(440,355,440 + 64,355 + 128))
        #Right left arm
        self.template.paste(self.tallrectangle,(506,355,506 + 64,355 + 128))
        #Up left arm
        self.template.paste(self.smallsquare,(308,289,308 + 64,289 + 64))
        #Down left arm
        self.template.paste(self.smallsquare,(308,485,308 + 64,485 + 64))

        self.template.save("out." + self.fileType)

        self.link = pyanonfile.upload('out.' + self.fileType)

        return(self.link.getLink())

if __name__ == "__main__":
    import hanger

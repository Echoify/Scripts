#/usr/bin/python

import sys, os
sys.path.append("../lib")

import Echoify
from PIL import Image

Echoify.writePlain("Please provide the original picture.")

while True:
    fileName = Echoify.readFileRef()
    if fileName is not None:
        img = Image.open(fileName)
        newImg = img.transpose(Image.FLIP_LEFT_RIGHT)
        path, ext = os.path.splitext(fileName)
        newPath = "%s.tr%s" % (path, ext)
        newImg.save(newPath)
        Echoify.writeFileRef(newPath)
        
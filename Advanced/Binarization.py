#/usr/bin/python

import sys, os
sys.path.append("../lib")

import Echoify
from PIL import Image

Echoify.writePlain("Please provide the original picture.")

while True:
    fileName = Echoify.readFileRef()
    if fileName is not None:
        col = Image.open(fileName)
        gray = col.convert('L')
        bw = gray.point(lambda x: 0 if x<128 else 255, '1')
        path, ext = os.path.splitext(fileName)
        newPath = "%s.bin%s" % (path, ext)
        bw.save(newPath)
        Echoify.writeFileRef(newPath)
        
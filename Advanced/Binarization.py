#/usr/bin/python

import sys, os
sys.path.append("../lib")

import Echonify
from PIL import Image

Echonify.writePlain("Please provide the original picture.")

while True:
    fileName = Echonify.readFileRef()
    if fileName is not None:
        col = Image.open(fileName)
        gray = col.convert('L')
        bw = gray.point(lambda x: 0 if x<128 else 255, '1')
        path, ext = os.path.splitext(fileName)
        newPath = "%s.bin%s" % (path, ext)
        bw.save(newPath)
        Echonify.writeFileRef(newPath)
        
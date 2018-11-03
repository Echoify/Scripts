#!/usr/bin/python

import sys
sys.path.append("../lib")

import Echoify
import hashlib

Echoify.writePlain("Please provide the original file, and I'll calculate the MD5 value.")

def md5(fileName):
    hash_md5 = hashlib.md5()
    with open(fileName, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

while True:
    fileName = Echoify.readFileRef()
    if fileName is not None:
        md5_str = md5(fileName)
        Echoify.writePlain("The MD5 value of the file is **%s**" % md5_str, "markdown")

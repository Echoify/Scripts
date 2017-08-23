#!/usr/bin/python

import sys
sys.path.append("../lib")

import Echonify
import hashlib

Echonify.writePlain("Please provide the original file, and I'll calculate the MD5 value.")

def md5(fileName):
    hash_md5 = hashlib.md5()
    with open(fileName, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

while True:
    fileName = Echonify.readFileRef()
    if fileName is not None:
        md5_str = md5(fileName)
        Echonify.writePlain("The MD5 value of the file is **%s**" % md5_str, "markdown")

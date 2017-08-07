#!/bin/bash

echo "Welcome to use CheckSum, Pass me the file path, and I'll help you figure out the MD5 value."

function calc {
    read path

    if [ -e "${path}" ]
    then
        md5 "${path}"
    else
        echo "Invalid file path, Please enter again."
    fi
    calc
}

calc

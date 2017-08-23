#!/bin/bash

echo "Please provide the original file, and I'll calculate the MD5 value."

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

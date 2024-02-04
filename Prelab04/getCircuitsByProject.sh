#!/bin/bash

# ######################################################
# Author : < Aidan Dannhausen-Brun >
# email : < adannhau@purdue.edu >
# ID : < ee364a10 >
# Date : < 2/4/2024 >
# ######################################################
# Write your sequence of statements here .

if [ $# -eq 0 ]; then
    echo "please specify a project"
    exit 1
fi

cd maps

grep $1 projects.dat | awk '{print $1}' | sort -u


exit 0
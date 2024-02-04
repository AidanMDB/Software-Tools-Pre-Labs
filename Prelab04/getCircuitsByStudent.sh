#!/bin/bash

# ######################################################
# Author : < Aidan Dannhausen-Brun >
# email : < adannhau@purdue.edu >
# ID : < ee364a10 >
# Date : < 2/4/2024 >
# ######################################################
# Write your sequence of statements here .

if [ $# -eq 0 ]; then
    echo "please specify a student"
    exit 1
fi


student_id=$(grep "$1" maps/students.dat | awk '{print $4}')     # gets student id from the given name
echo "$(grep -lr "$student_id" circuits | egrep -o "[0-9]{2}-[0-9]-[0-9]{2}" | sort -u)"        # searches all files in circuits directory that have the student_id


exit 0
#!/bin/bash

# ######################################################
# Author : < Aidan Dannhausen-Brun >
# email : < adannhau@purdue.edu >
# ID : < ee364a10 >
# Date : < 2/4/2024 >
# ######################################################
# Write your sequence of statements here .

echo "$(bash getCircuitsByStudent.sh $1 | xargs -I {} wc -c circuits/circuit_{}.dat | sort -hr | head -n 1 | egrep -o "[0-9]{2}-[0-9]-[0-9]{2}")"
#          ^ get the stuents circuits       ^ pass those values into wc as files    ^ top-down  ^ grab 1st line       ^ grab the circuit name back out of the file name

#awk might make this simpler

exit 0
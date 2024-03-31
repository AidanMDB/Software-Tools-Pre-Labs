#!/bin/bash

# ######################################################
# Author : < Aidan Dannhausen-Brun >
# email : < adannhau@purdue.edu >
# ID : < ee364a10 >
# Date : < 2/4/2024 >
# ######################################################
# Write your sequence of statements here .


# if [check if the file is there]
#       for error handling
frist_count=$(bash getComponentUseCount.sh $1)
second_count=$(bash getComponentUseCount.sh $2)

if [ "$frist_count" -lt "$second_count" ];
then
    echo "$2"
else
    echo "$1"
fi

exit 0
#!/bin/bash

# ######################################################
# Author : < Aidan Dannhausen-Brun >
# email : < adannhau@purdue.edu >
# ID : < ee364a10 >
# Date : < 2/4/2024 >
# ######################################################
# Write your sequence of statements here .

echo "$(grep -lr "$1" circuits | wc -w)"    # searches circuits directory for all files that contain the component
                                            # those files are essentially a string and each file is its own word 
                                            # so I can just count the words

exit 0
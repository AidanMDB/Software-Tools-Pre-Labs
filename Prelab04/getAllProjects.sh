#!/bin/bash

# ######################################################
# Author : < Aidan Dannhausen-Brun >
# email : < adannhau@purdue.edu >
# ID : < ee364a10 >
# Date : < 2/4/2024 >
# ######################################################
# Write your sequence of statements here .

echo "$(egrep -o "[A-Z0-9]+-[A-Z0-9]+-[A-Z0-9]+-[A-Z0-9]+-[A-Z0-9]+" $1 | sort -u | tr -d '-')"

# awk command 

exit 0
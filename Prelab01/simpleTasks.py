# ######################################################
# Author :      Aidan Dannhausen-Brun
# email :       adannhau@purdue.edu
# ID :          ee364a10
# Date :        1/14/24
# ######################################################

import os # List of module import statements
import sys # Each one on a line

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def writePyramids (filePath, baseSize: int, count: int, char: str) -> float :
    pyramid_char = []

    for i in range(0, baseSize, 2):
        char_this_row = char * (i + 1)               # determines the number of characters in the row
        pyramid_char.append(char_this_row.center(baseSize))    # centers those characters
        # print(char_this_row)

    file = open(filePath, "w")

    for line in pyramid_char:
        for i in range(count):

            file.write(line)
            if i != count - 1:      # makes sure space doesn't end up at the end of the line
                file.write(" ")

        file.write("\n")

    file.close()




# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
# Write anything here to test your code .
    

writePyramids("pyramid13_test.txt", 13, 6, 'X')
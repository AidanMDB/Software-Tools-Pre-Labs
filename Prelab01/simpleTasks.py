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

def writePyramids (filePath: str, baseSize: int, count: int, char: str):
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

def getStreaks(sequence: str, letters: str) -> list:
    all_streaks = []

    temp_letter = sequence[0]
    streak = ""

    for letter in sequence:             # generates every streak of letters and puts them in a list
        if temp_letter == letter: 
            streak += letter
        else:
            all_streaks.append(streak)
            temp_letter = letter
            streak = letter
    all_streaks.append(streak)


    streak_list = []

    for stk in all_streaks:             # checks if the letters matches the streaks
        for let in letters:
            if let == stk[0]:
                streak_list.append(stk)

    return streak_list

# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
# Write anything here to test your code .
    

#writePyramids("pyramid13_test.txt", 13, 6, 'X')
#writePyramids("puramid15_test.txt", 15, 5, "*")

sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
print(getStreaks(sequence, "PAZ"))
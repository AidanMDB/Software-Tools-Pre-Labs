# ######################################################
# Author : Aidan Dannhausen-Brun
# email : adannhau@purdue.edu
# ID : ee364a10
# Date : 3/3/2024
# ######################################################

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def convertToInteger(boolList):
    if not isinstance(boolList, list) or boolList == []:
        return None
    
    if not all(isinstance(element, bool) for element in boolList):
        return None

    binary_string = ""
    for b in boolList:
        if b:
            binary_string += "1"
        else:
            binary_string += "0"

    return int(binary_string, 2)


# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
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

def converToBoolean(num, size):
    if not (isinstance(num, int) and isinstance(size, int)):
        raise ValueError("Inputs should be integers")

    binary_rep = f'{num:{size}b}'
    bool_list = []
    for b in binary_rep:
        if b == '1':
            bool_list.append(True)
        else:
            bool_list.append(False)

    return bool_list


# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################

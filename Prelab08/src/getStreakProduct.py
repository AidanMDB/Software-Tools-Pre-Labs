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

def calc_product(sequence):
    calc = 1
    for digit in sequence:
        calc *= int(digit)
    return calc


def sub_sequences(sequence, size):
    sub_sequences = []
    for i in range(len(sequence) - size + 1):
        sub_sequences.append((sequence[i:i+size], i))
    return sub_sequences


def sort_subsequences(index):
    return index[1]


def getStreakProduct(sequence, maxsize, product):
    matching = []
    for size in range(2, maxsize + 1):
        subsequences = sub_sequences(sequence, size)
        for sub in subsequences:
            if calc_product(sub[0]) == product:
                matching.append(sub)

    matching.sort(key=sort_subsequences)
    return [match[0] for match in matching]


# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################


# ######################################################
# Author :      Aidan Dannhausen-Brun
# email :       adannhau@purdue.edu
# ID :          ee364a10
# Date :        3/6/24
# ######################################################

import random as rng

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################


def getStreaks(sequence: str, letters: str) -> list:
    if not isinstance(sequence, str):
        raise TypeError("Sequence must of string type")

    if not isinstance(letters, str):
        raise TypeError("Letters must be of string type")

    if len(sequence) > 1000:
        raise OverflowError("Sequence must be less than 1000 characters")

    if len(letters) > 1000:
        raise OverflowError("Letters must be less than 1000 characters")

    all_streaks = []

    temp_letter = sequence[0]
    streak = ""

    # generates every streak of letters and puts them in a list
    for letter in sequence:
        if temp_letter == letter:
            streak += letter
        else:
            all_streaks.append(streak)
            temp_letter = letter
            streak = letter
    all_streaks.append(streak)

    streak_list = []

    # checks if the letters matches the streaks
    for stk in all_streaks:
        for let in letters:
            if let == stk[0]:
                streak_list.append(stk)

    return streak_list


def string_fuzzer():
    string_length = rng.randrange(0, 100000)
    out = ""
    for i in range(0, string_length):
        out += chr(rng.randrange(32, 126))
    return out


def num_fuzzer():
    num = rng.randrange(-20000000000000, 20000000000000)
    return num


def trials_numFuzzer(num_trials: int):
    for i in range(num_trials):
        input1 = num_fuzzer()
        input2 = num_fuzzer()
        try:
            output = getStreaks(input1, input2)
            print(output)
        except TypeError:
            print("Type error for inccorect type")
        continue


def trials_stringFuzzer(num_trials: int):
    for i in range(num_trials):
        input1 = string_fuzzer()
        input2 = string_fuzzer()
        try:
            getStreaks(input1, input2)
            # print(output)
        except TypeError:
            print("Type error for inccorect type")
            continue
        except OverflowError:
            print("Overflow error string to large")
            continue

# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
# Write anything here to test your code .


#
# print(string_fuzzer())
# print(string_fuzzer())
# print(num_fuzzer())
# print(num_fuzzer())
trials_numFuzzer(10)
trials_stringFuzzer(10)

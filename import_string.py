# import string
# checked = 0
from ast import Num
from typing import final


def check(string):
    checked = 0
    final_number = 0
    for i, num in enumerate(string):
        if (i+1) % 2 == 0:
            checked += (int(num) * 2)
            if int(num) > 5:
                checked -= 9
            # checked += int(num)
        else:
            checked += (int(num) * 1)
            # checked += int(num)
    # print(num)
    print(checked)

    final_number = 10 - (int(checked) % 10)
    # final_final_number = final_number
    print(final_number)
    return(final_number)
    # return(final)

# final_final_number = final_number
check("7992739871")

# print(checked_chec)

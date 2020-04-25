# Python3 program to Convert positive
# list integers to negative and vice-versa
L = list(map(int, input().split()))


def convert(li):
    return [-index for index in li]


li_in = L
print(convert(li_in))


# 2
# import numpy as np
# def Convert(lst):
#     lst = np.array(lst)
#     return list(-lst)
# # Driver code
# lst = [-1, 2, 3, -4, 5, -6, -7]
# print(Convert(lst))

# Задача 1
# import math as m
#
# n1 = float(input())
# n2 = float(input())
# n3 = float(input())
# n4 = float(input())
# result = m.floor((n1 + n2) / n3) * n4
# print(int(result))


# Задача 2 (INTERPOLATION)
# in1 = input()
# in2 = input()
# in3 = input()
# print(f'{in1}{in3}{in2}')


# Задача 3 - ELEVATOR (IF)
# import math as m
#
# n_people = int(input())
# elevator_capacity = int(input())
# courses = n_people / elevator_capacity
# last_people = n_people % elevator_capacity
# if last_people != 0 and last_people < elevator_capacity:
#     courses += 1
# print(m.floor(courses))


# Задача 4 (FOR)
# n = int(input())
# count_ascii = 0
# for counter in range(1, n + 1):
#     char_in = ord(input())
#     count_ascii += char_in
# print(f'The sum equals: {count_ascii}')


# Задача 5 (FOR)
# start_index = int(input())
# stop_index = int(input())
# for index in range(start_index, stop_index + 1):
#     ascii_char = chr(index)
#     print(ascii_char, end=' ')


# Задача 6 (Triple FOR) ord('a')
# n = int(input())
# collection = []
# for code in range(ord('a'), n + ord('a')):
#     collection.append(chr(code))
# for first_char in collection:
#     for second_char in collection:
#         for third_char in collection:
#             print(f'{first_char}{second_char}{third_char}')


# Задача 7 (FOR)
# CAPACITY = 255  # liters
# n_lines = int(input())
# total_liters = 0
# for line in range(1, n_lines + 1):
#     add_liters = int(input())
#     if total_liters + add_liters > CAPACITY:
#         print('Insufficient capacity!')
#         continue
#     else:
#         total_liters += add_liters
# print(total_liters)


# Задача 8* "Party Profit" ************************************************** HARD
# import math as m
#
# party_size = int(input())
# days = int(input())
#
# companions = party_size
# coins = 0.0
#
# for day in range(1, days + 1):
#     # START of the 10th day: 2 of companions must leave.
#     if day % 10 == 0:
#         companions -= 2
#     # START of the 15th day: 5 companions must join the adventure.
#     if day % 15 == 0:
#         companions += 5
#
#     # Income and outcome EVERY DAY
#     coins += 50
#     coins -= (2 * companions)
#
#     if day % 3 == 0:
#         coins -= 3 * companions
#
#     if day % 5 == 0:
#         coins += 20 * companions
#         if day % 3 == 0:
#             coins -= 2 * companions
#
# print(f"{companions} companions received {m.floor(coins / companions)} coins each.")
#
# li = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x*2, li)))

from collections import deque

liters = int(input())
queue = deque()
while True:
    inp = input()
    if inp == "Start":
        break
    else:
        queue.append(inp)

while True:
    inp = input()
    if inp == "End":
        print(f"{liters} liters left")
        break
    else:
        inp = inp.split()
        if len(inp) == 1:
            digit = int(inp[0])
            if liters - digit >= 0:
                print(f"{queue.popleft()} got water")
                liters -= digit
            else:
                print(f"{queue.popleft()} must wait")
                continue
        else:
            value = int(inp[1])
            liters += value
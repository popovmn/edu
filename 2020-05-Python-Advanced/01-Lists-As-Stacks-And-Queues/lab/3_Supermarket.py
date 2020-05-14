# #QUEUE - опашки (първи влиза - първи излиза)
# from collections import deque as queue
# queue = queue()
#
# while True:
#     inp = input()
#     if inp == "End":
#         print(f"{len(set(queue))} people remaining.")
#         break
#     elif inp == "Paid":
#         while queue:
#             print(queue.popleft())
#     else:
#         queue.append(inp)


#QUEUE - опашки (първи влиза - първи излиза)
queue = []

while True:
    inp = input()
    if inp == "End":
        print(f"{len(set(queue))} people remaining.")
        break
    elif inp == "Paid":
        while queue:
            print(queue.pop(0))
    else:
        queue.append(inp)




# QUEUES
from collections import deque

total_liters = int(input())
people = deque()

while True:
    # Name or END command
    cmd = input()
    if cmd == "Start":
        while True:
            cmd2 = input()
            if cmd2 == "End":
                print(f"{total_liters} liters left")
                break

            if "refill" in cmd2:
                cmd2 = cmd2.split()[1]
                total_liters += int(cmd2)
            elif cmd2.isdigit():
                print(f"{people[0]} got water")
                people.popleft()
                print(people)
                total_liters -= int(cmd2)
    else:
        people.append(cmd)
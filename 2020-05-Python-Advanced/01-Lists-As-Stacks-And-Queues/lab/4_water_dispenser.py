# QUEUES
from collections import deque

def add_liters(tl, c):
    pass

def subtract_liters():
    pass


def start():
    total_liters = int(input())
    people = deque()
    while True:
        cmd = input()
        if cmd.startswith('Start'):

            while people:
                cmd = input()

                if cmd.startswith('End'):
                    break

                if cmd.startswith('refill'):
                    total_liters += int(cmd.split()[1])
                    continue

                elif cmd.isdigit():
                    if total_liters < int(cmd):
                        print(f"{people.popleft()} must wait")
                    else:
                        total_liters -= int(cmd)
                        print(f"{people.popleft()} got water")
                        # трябва да е people[0] вместо people.popleft()
                        # поредното глупаво условие
            print(f"{total_liters} liters left")
            break
        else:
            people.append(cmd)


if __name__ == '__main__':
    start()






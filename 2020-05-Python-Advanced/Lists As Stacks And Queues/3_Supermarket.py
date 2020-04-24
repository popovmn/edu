from collections import deque

# creates empty queue named "names"
names = deque()

while True:
    command = input()
    if command == "End":
        print(f"{names.__len__()} people remaining.")
        break
    elif command == "Paid":
        # while we do have people in queue
        while names:
            print(names.popleft())
    else:
        names.append(command)




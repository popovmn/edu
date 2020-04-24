# cat 10|potion 30|orc 10|chest 10|snake 25|chest 110

input_string = input().split("|")
health = 100
bitcoins = 0
best_room_index = 0
best_room_result = 0
you_died = False

for cmd2 in input_string:
    cmd = cmd2.split()
    if cmd[0] == "potion":
        diff = 0
        if int(cmd[1]) + health > 100:
            diff = 100 - ((health + int(cmd[1])) - int(cmd[1]))
            health = 100
        else:
            diff = int(cmd[1])
            health += int(cmd[1])

        print(f'You healed for {diff} hp.')
        print(f'Current health: {health} hp.')
        continue

    elif cmd[0] == "chest":
        bitcoins += int(cmd[1])
        print(f'You found {cmd[1]} bitcoins.')
        continue

    else:
        # you fight a monster
        health -= int(cmd[1])

    if health > 0:
        print(f'You slayed {cmd[0]}.')
    else:
        print(f'You died! Killed by {cmd[0]}.')
        print(f'Best room: {input_string.index(cmd2) + 1}')
        you_died = True
        break

if not you_died:
    print(f'You\'ve made it!')
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')


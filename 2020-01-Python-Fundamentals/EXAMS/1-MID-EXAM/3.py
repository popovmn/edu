input_string = input().split(', ')

while True:
    command = input()
    if 'Craft!' in command:
        break
    else:
        command = command.split(' - ')
        if command[0] == "Collect" and command[1] not in input_string:
            input_string.append(command[1])
        elif command[0] == "Drop" and command[1] in input_string:
            input_string.remove(command[1])
        elif command[0] == "Combine Items":
            combine_command = command[1].split(':')
            if combine_command[0] in input_string:
                old_word_index = input_string.index(combine_command[0]) + 1
                input_string.insert(old_word_index, combine_command[1])
        elif command[0] == "Renew" and command[1] in input_string:
            input_string.append(input_string.pop(input_string.index(command[1])))

print(", ".join(input_string))
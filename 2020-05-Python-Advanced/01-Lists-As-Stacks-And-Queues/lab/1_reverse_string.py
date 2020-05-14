# string = input()
# print("".join(reversed(string)))


#print(input()[::-1])


# string = list(input())
# s = []
# for i in range(len(string)):
#     s.append(string.pop())
# print("".join(s))


def start(usr_in):
    while usr_in:
        print("".join(usr_in.pop()))


user_input = list(input())

if __name__ == "__main__":
    start(user_input)


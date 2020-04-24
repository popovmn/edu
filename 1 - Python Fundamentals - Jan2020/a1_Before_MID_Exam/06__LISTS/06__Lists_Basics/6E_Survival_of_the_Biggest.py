li_of_int = list(map(int, input().split()))
nums_to_remove = int(input())


def remove():
    for i in range(nums_to_remove):
        li_of_int.remove(min(li_of_int))
    print(li_of_int)


remove()

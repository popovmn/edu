str_li = list(map(int, input().split(', ')))
n_beggars = int(input())
new_li = []

if len(str_li) > n_beggars:
    for index in range(n_beggars):
        temp = 0
        for num in range(index, len(str_li), n_beggars):
            temp += str_li[num]
        new_li.append(temp)
elif len(str_li) < n_beggars:
    new_li = str_li
    while len(new_li) < n_beggars:
        new_li.append(0)
else:
    new_li = str_li

print(new_li)

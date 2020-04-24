factor = int(input())
count = int(input())
num_list = []
multiplied = factor * count

for i in range(factor, multiplied + 1, factor):
    num_list.append(i)

print(num_list)

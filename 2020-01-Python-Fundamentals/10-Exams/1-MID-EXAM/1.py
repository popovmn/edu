
count_of_students = int(input())
count_of_lectures = int(input())
initial_bonus = int(input())

all_attends = []
all_bonuses = []

for s in range(1, count_of_students + 1):
    attendances = int(input())
    all_bonuses.append(round(attendances / count_of_lectures * (5 + initial_bonus)))
    all_attends.append(attendances)

max_bonus = max(all_bonuses)

max_bonus_i = all_bonuses.index(max_bonus)

current_student_attends = all_attends[max_bonus_i]

print(f'Max Bonus: {max_bonus}.\nThe student has attended {current_student_attends} lectures.')
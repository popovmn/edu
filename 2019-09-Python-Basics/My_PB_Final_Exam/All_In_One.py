
# 1
air_ticket_price_going = float(input())
air_ticket_price_return = float(input())
ticket_game_price = float(input())
num_games = int(input())
percent_of_discount = int(input())
people = 1 + 5  # :D
sum_air_tickets = people * (air_ticket_price_going + air_ticket_price_return)
discounted_air_tickets = sum_air_tickets - sum_air_tickets * (percent_of_discount/100)
total_sum_game_tickets = people * num_games * ticket_game_price
total = discounted_air_tickets + total_sum_game_tickets
sum_per_friend = total / people
print(f'Total sum: {total:.2f} lv.')
print(f'Each friend has to pay {sum_per_friend:.2f} lv.')

# 2
t_shirt_price = float(input())
needed = float(input())
shirt_price = t_shirt_price * 0.75
socks_price = shirt_price * 0.20
sneakers_price = (t_shirt_price + shirt_price) * 2
total = t_shirt_price + shirt_price + socks_price + sneakers_price
total -= total * 0.15
if total >= needed:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total:.2f} lv.')
else:
    diff = abs(total - needed)
    print('No, he will not earn the world-cup replica ball.')
    print(f'He needs {diff:.2f} lv. more.')

# 3
budget = float(input())
city = input()
nights = int(input())
night_price = 0
two_way_ticket = 0
discount = 0
if city == 'Cairo':
    night_price = (250 * 2) * nights
    two_way_ticket = 600
if city == 'Paris':
    night_price = (150 * 2) * nights
    two_way_ticket = 350
if city == 'Lima':
    night_price = (400 * 2) * nights
    two_way_ticket = 850
if city == 'New York':
    night_price = (300 * 2) * nights
    two_way_ticket = 650
if city == 'Tokyo':
    night_price = (350 * 2) * nights
    two_way_ticket = 700
total = night_price + two_way_ticket
if 1 <= nights <= 4:
    if city == 'Cairo' or city == 'New York':
        total -= total * 0.03
elif 5 <= nights <= 9:
    if city == 'Cairo' or city == 'New York':
        total -= total * 0.05
    elif city == 'Paris':
        total -= total * 0.07
elif 10 <= nights <= 24:
    if city == 'Cairo':
        total -= total * 0.1
    elif city == 'Paris' or city == 'New York' or city == 'Tokyo':
        total -= total * 0.12
elif 25 <= nights <= 49:
    if city == 'Tokyo' or city == 'Cairo':
        total -= total * 0.17
    elif city == 'New York' or city == 'Lima':
        total -= total * 0.19
    elif city == 'Paris':
        total -= total * 0.22
elif nights >= 50:
    total -= total * 0.3
diff = abs(budget - total)
if total < budget:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')

# 4
team = input()
n_games = int(input())
scores = 0
diff = 0
for game in range(1, n_games + 1):
    goals_plus = int(input())
    goals_minus = int(input())
    if goals_plus > goals_minus:
        scores += 3
    elif goals_plus == goals_minus:
        scores += 1
    diff += (goals_plus - goals_minus)
if diff >= 0:
    print(f'{team} has finished the group phase with {scores} points.')
    print(f'Goal difference: {diff}.')
else:
    print(f'{team} has been eliminated from the group phase.')
    print(f'Goal difference: {diff}.')

# 5
months = int(input())
electricity_tax = 0
electricity = 0
water = 0
internet = 0
other = 0
average = 0
for month in range(1, months + 1):
    electricity_tax = float(input())
    electricity += electricity_tax
    water += 20
    internet += 15
    percent20 = (electricity + water + internet) * 0.2
    other = electricity + water + internet + percent20
average = (electricity + water + internet + other) / months
print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')

# 6
num_locations = int(input())
for location in range(num_locations):
    planned_kg_gold = float(input())
    days_in_current_location = int(input())
    gold_location = 0
    for day in range(days_in_current_location):
        gold_for_current_day = float(input())
        gold_location += gold_for_current_day
        average = gold_location / days_in_current_location
    if average < planned_kg_gold:
        diff = abs(average - planned_kg_gold)
        print(f'You need {diff:.2f} gold.')
    else:
        print(f'Good job! Average gold per day: {average:.2f}.')
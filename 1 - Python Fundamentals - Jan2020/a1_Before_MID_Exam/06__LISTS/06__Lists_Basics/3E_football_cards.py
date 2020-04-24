cards = input().split()
MAX_PLAYERS = 11
a_players = [str(player) for player in range(1, MAX_PLAYERS+1)]
b_players = [str(player) for player in range(1, MAX_PLAYERS+1)]

for card in cards:
    if card[0] == 'A':
        a_players_out = card.replace('A-', '')
        if a_players_out in a_players:
            a_players.remove(a_players_out)
    elif card[0] == 'B':
        b_players_out = card.replace('B-', '')
        if b_players_out in b_players:
            b_players.remove(b_players_out)

if len(a_players) < 7 or len(b_players) < 7:
    print(f'Team A - {len(a_players)}; Team B - {len(b_players)}')
    print('Game was terminated')
else:
    print(f'Team A - {len(a_players)}; Team B - {len(b_players)}')
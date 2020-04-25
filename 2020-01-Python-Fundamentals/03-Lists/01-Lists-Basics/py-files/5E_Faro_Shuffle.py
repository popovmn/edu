cards = input().split()
half = int(len(cards) / 2)
n_shuffles = int(input())


def faro_shuffle():
    global cards
    half_ = cards[half:]
    _half = cards[:half]

    cards.clear()
    for index in range(len(half_)):
        cards.append(_half[index])
        cards.append(half_[index])


for every_shuffle in range(n_shuffles):
    faro_shuffle()

print(cards)

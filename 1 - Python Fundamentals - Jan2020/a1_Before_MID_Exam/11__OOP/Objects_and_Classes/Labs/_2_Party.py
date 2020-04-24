class Person:
    def __init__(self, name):
        self.name = name


class Party:
    def __init__(self):
        self.people = []


party = Party()
command = ''

while Party:
    command = input()
    if command == 'End':
        break
    else:
        person = command
        person = Person(person)

        party.people.append(person.name)

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")

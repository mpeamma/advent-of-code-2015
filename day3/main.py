f = open("input", "r")
contents = f.read()

locations = [(0,0)]
current = [(0,0), (0,0)]
turn = 0

for i in contents:
    if i == '^':
        current[turn] = (current[turn][0], current[turn][1] + 1)
    elif i == '<':
        current[turn] = (current[turn][0] - 1, current[turn][1])
    elif i == '>':
        current[turn] = (current[turn][0] + 1, current[turn][1])
    elif i == 'v':
        current[turn] = (current[turn][0], current[turn][1] - 1)

    if current[turn] not in locations:
        locations = [current[turn]] + locations
    turn = (turn + 1) % 2

print(len(locations))

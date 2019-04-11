f = open("input.txt", "r")
contents = f.read()
up = contents.count('(')
down = contents.count(')')
print(up - down)

up = 0
down = 0
count = 1
for i in contents:
    if i == '(':
        up += 1
    elif i == ')':
        down += 1

    if down > up:
        print(count)
        break
    count += 1

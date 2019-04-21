f = open("input", "r")
contents = f.readlines()

grid = [[0 for x in range(0,1000)] for y in range(0, 1000)]

def doOperation(start, end, operation):
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            grid[x][y] = operation(grid[x][y])

for line in contents:
    words = line.strip().split()
    if words[0] == "turn":
        indexes = (2, 4)
        if words[1] == "on":
            def f(x): return x + 1 
        elif words[1] == "off":
            def f(x): return x - 1 if x > 0 else 0
    elif words[0] == "toggle":
        indexes = (1,3)
        def f(x): return x + 2
    
    start_coords = [int(x) for x in words[indexes[0]].split(',')]
    end_coords = [int(x) for x in words[indexes[1]].split(',')]
        
    doOperation(start_coords, end_coords, f)

print(sum([sum([y for y in x]) for x in grid]))

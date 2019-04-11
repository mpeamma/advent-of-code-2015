f = open("input", "r")
contents = f.readlines()

paper = 0
ribbon = 0
for line in contents:
    dims = [int(x) for x in line.strip().split('x')] 
    
    sizes = [dims[0] * dims[1], dims[0] * dims[2], dims[1] * dims[2]]
    extra = min(sizes)
    area = 2 * (sizes[0] + sizes[1] + sizes[2]) + extra

    perim = 2 * (sum(dims) - max(dims)) + (dims[0] * dims[1] * dims[2])

    ribbon += perim
    paper += area

print(paper)
print(ribbon)

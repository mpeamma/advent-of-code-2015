import re

f = open("input", "r")
contents = f.readlines()

class Node:
    def __init__(self, inputs, output, operation = "PASS"):
        self.inputs = inputs
        self.output = output
        self.operation = operation

nodes = []        
cache = {"b": 16076}
def find_node(node):
    return next(x for x in nodes if x.output == node)

def addToCache(value, key):
    cache[key] = value
    return value

def resolve(node):
    if node.output in cache.keys():
        return cache[node.output]

    total = 0
    if node.operation == "PASS":
        isNum = bool(re.match(r'^\d+$', node.inputs[0]))
        if isNum:
            return addToCache(int(node.inputs[0]), node.output)
        else:
            return addToCache(resolve(find_node(node.inputs[0])), node.output)
    elif node.operation == "NOT":
        return addToCache(65535 - resolve(find_node(node.inputs[0])), node.output)
    else:
        isNum = bool(re.match(r'^\d+$', node.inputs[0]))
        input1 = int(node.inputs[0]) if isNum else resolve(find_node(node.inputs[0]))
        isNum = bool(re.match(r'^\d+$', node.inputs[1]))
        input2 = int(node.inputs[1]) if isNum else resolve(find_node(node.inputs[1]))

        if node.operation == "LSHIFT":
            return addToCache(input1 << input2, node.output)
        elif node.operation == "RSHIFT":
            return addToCache(input1 >> input2, node.output)
        elif node.operation == "AND":
            return addToCache(input1 & input2, node.output)
        elif node.operation == "OR":
            return addToCache(input1 | input2, node.output)

for line in contents:
    tokens = line.strip().split()
    #simple value exchange
    if len(tokens) == 3:
        nodes.append(Node([tokens[0]], tokens[2]))
    #NOT 1 Input
    if len(tokens) == 4:
        nodes.append(Node([tokens[1]], tokens[3], tokens[0]))
    #2 Inputs and Operation
    if len(tokens) == 5:
        nodes.append(Node([tokens[0], tokens[2]], tokens[4], tokens[1]))

a = find_node('a')
print(resolve(a))
print(cache)

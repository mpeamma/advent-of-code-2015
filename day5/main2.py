import re
f = open("input", "r")
contents = f.readlines()

good_strings = 0
for line in contents:
    line = line.strip()
    rule1 = bool(re.search(r'(..).*\1', line))
    rule2 = bool(re.search(r'(.).\1', line)) 
    if rule1 and rule2: 
        good_strings += 1

print(good_strings)

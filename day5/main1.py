import re
f = open("input", "r")
contents = f.readlines()

good_strings = 0
for line in contents:
    line = line.strip()
    vowels = len(re.findall("[aeiou]", line))
    has_double = bool(re.search(r'(.)\1', line))
    bad_strings = "ab" in line or "cd" in line or "pq" in line or "xy" in line
    if(has_double):
        print(line)
    if vowels >= 3 and has_double and not bad_strings: 
        good_strings += 1

print(good_strings)

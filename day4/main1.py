import hashlib 
  
# initializing string 
secret = "yzbqklnj"
result = "test"  

counter = -1
while result[:6] != "000000":
    counter += 1
    test = secret + str(counter)
    result = hashlib.md5(test.encode()).hexdigest()
    #print(test)

print(counter)

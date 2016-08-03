table = [[] for x in range(10)]

def hash_function(key): return key % 10

def insert(table,input,value): table[hash_function(input)].append((input,value))

def get(table,key):
  # get index by hashing the key
  # traverse list at key
  for item in table[hash_function(key)]:
    if item[0] == key:
      return item[1]


def fold(input):
  # let's fold phone numbers e.g. 342-987-0929
  # divide input into equal parts (last part may not be equal)
  # add parts together and hash to find key

  total = 0

  # while input has 2 or more characters
  # parse an int from those chars
  # add int to the running total

  while len(input) > 1:     
   total += int(input[:2].strip('-'))
   input = input[2:]
  
  return total


insert(table,41,'apple')
insert(table,93,'banana')
insert(table,13,'tangerine')
insert(table,1141,'grapefruit')
insert(table,hash_function(fold('543-321-9876')),'543-321-9876')

print(table)

print('value at key 93: ' + get(table,93))
print('value at key 13: ' + get(table,13))

# print(fold('543-321-9876'))
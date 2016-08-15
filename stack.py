from stack_obj import Stack

s = Stack()

strToReverse = 'apple'
reversedStr = ''

for theChar in strToReverse:
  s.push(theChar)

print(s.items)

while len(s.items) > 0:
  reversedStr = reversedStr + s.pop()

print(reversedStr)

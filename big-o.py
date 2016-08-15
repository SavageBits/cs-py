numbers = [1,4,5,2,3,9,0]

# O(n)
def getMinOn(listOfNumbers):
  minNum = listOfNumbers[0]
  i = 1

  while i < len(listOfNumbers):
    if minNum > listOfNumbers[i]:
      minNum = listOfNumbers[i]

    i += 1;

  return minNum;

# O(n2)
def getMinOn2(listOfNumbers):
  minNum = listOfNumbers[0]
  
  for i in listOfNumbers:
    for j in listOfNumbers:
      if i > j:
        minNum = j
    
  return minNum

print getMinOn(numbers)
print getMinOn2(numbers)

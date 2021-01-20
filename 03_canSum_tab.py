def canSum(targetSum :int , numbers: [int]):
  table = [False]*(targetSum+1)
  table[0] = True
  for i in range(targetSum+1):
    if(table[i]):
      for num in numbers:
        if ((i+num)<=targetSum):
          table[i+num]=True
  return table[targetSum]

print(canSum(7,[2,3])) #true
print(canSum(7,[5,3,4,7])) #true
print(canSum(7,[2,4])) #false
print(canSum(8,[2,3,5])) #true
print(canSum(300,[7,14])) #false
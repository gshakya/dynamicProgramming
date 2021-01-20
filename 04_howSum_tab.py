def howSum(targetSum :int , numbers: [int]):
  table = [None]*(targetSum+1)
  table[0] = []
  for i in range(targetSum+1):
    if(table[i] != None):
      for num in numbers:
        if ((i+num)<=targetSum):
          table[i+num]= [num]+table[i]        
  return table[targetSum]

print(howSum(7,[2,3])) #true
print(howSum(7,[5,3,4,7])) #true
print(howSum(7,[2,4])) #false
print(howSum(8,[2,3,5])) #true
print(howSum(300,[7,14])) #false

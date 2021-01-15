def howSum(targetSum : int,numbers : [int] , memo = None):
  if(memo==None):
    memo ={}
  if(targetSum == 0):
    return []
  if(targetSum < 0):
    return None
  if(targetSum in memo):
    return memo[targetSum]
  for n in numbers:
    remainder = targetSum-n
    result = howSum(remainder,numbers,memo)
    if(result != None):
      result.append(n)
      memo[remainder]=result
      return result
  memo[targetSum]=None
  return None

print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
print(howSum(300,[7,14]))


def howSum(targetSum : int,numbers : [int] ):
  if(targetSum == 0):
    return []
  if(targetSum < 0):
    return None
  for n in numbers:
    remainder = targetSum-n
    result = howSum(remainder,numbers)
    if(result != None):
      result.append(n)
      return result
  return None

print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
print(howSum(300,[7,14]))


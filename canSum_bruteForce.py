def canSum(targetSum : int,numbers : [int] ):
  if(targetSum == 0):
    return True
  if(targetSum < 0):
    return False
  for n in numbers:
    if(canSum(targetSum-n,numbers)):
      return True
  return False

print(canSum(7,[2,3]))
print(canSum(7,[5,3,4,7]))
print(canSum(7,[2,4]))
print(canSum(8,[2,3,5]))
print(canSum(300,[7,14]))


def canSum(targetSum : int,numbers : [int] ,memo = None):
  if(memo==None):
    memo ={}
  if(targetSum in memo):
    return memo[targetSum]
  if(targetSum == 0):
    return True
  if(targetSum < 0):
    return False  
  for n in numbers:
    remainder = targetSum-n    
    if(canSum(remainder,numbers,memo)):
      memo[remainder] = True
      return True
  memo[remainder]= False
  return False

print(canSum(7,[2,3])) #true
print(canSum(7,[5,3,4,7])) #true
print(canSum(7,[2,4])) #false
print(canSum(8,[2,3,5])) #true
print(canSum(300,[7,14])) #false


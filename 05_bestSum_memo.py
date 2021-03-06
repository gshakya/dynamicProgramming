def bestSum(targetSum : int,numbers : [int], memo = None ):
  if(memo==None):
    memo ={}
  if(targetSum in memo):
    return memo[targetSum]
  if(targetSum == 0):
    return []
  if(targetSum < 0):
    return None
  bestSumRes = None
  for n in numbers:
    remainder = targetSum-n
    result = bestSum(remainder,numbers ,memo)
    if(result != None):
      result.append(n)
      if(bestSumRes== None or len(result)<len(bestSumRes)):
        bestSumRes = result
  memo[targetSum] = bestSumRes
  return bestSumRes

print(bestSum(7,[2,3]))
print(bestSum(7,[5,3,4,7]))
print(bestSum(7,[2,4]))
print(bestSum(8,[2,3,5]))
print(bestSum(300,[7,14]))


def gridtraveller(m: int , n : int , memo: dict ={}):
  key =  str(m)+','+str(n)
  if (key in memo):
    return memo[key]
  if(m==0 or n ==0):
    return 0
  if ( m ==1 or n == 1):
    return 1
  memo[key] = gridtraveller(m-1,n, memo)+gridtraveller(m,n-1,memo)
  return gridtraveller(m-1,n, memo)+gridtraveller(m,n-1,memo)

print (gridtraveller(2,3))
print (gridtraveller(3,3))
print (gridtraveller(18,18))
  

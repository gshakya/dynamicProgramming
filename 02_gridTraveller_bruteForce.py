def gridtraveller(m: int , n : int):
  if(m==0 or n ==0):
    return 0
  if ( m ==1 or n == 1):
    return 1
  return gridtraveller(m-1,n)+gridtraveller(m,n-1)

print (gridtraveller(2,3))
print (gridtraveller(3,3))
print (gridtraveller(18,18))
  

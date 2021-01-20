from pprint import pprint
def gridTraveller(c : int , r : int):
  table = [[0]*(c+1) for x in range(r+1)]
  table[1][1] =1
  for i in range(r+1):
    for j in range(c+1):
      if((i+1)<=r):
       table[i+1][j]+= table[i][j]
      if((j+1)<=c):
       table[i][j+1]+= table[i][j]
  return table[r][c]

pprint (gridTraveller(2,3))
pprint (gridTraveller(3,3))
pprint (gridTraveller(18,18))
  
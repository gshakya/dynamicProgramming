def countConstruct(target : str, wordBank: [str]):
  tableLen = len(target)+1
  table = [0]*tableLen
  table[0]= 1
  for i in range(tableLen):
    if(table[i]):
      for word in wordBank:
          if(target.find(word,i)==i):
            wordLen= len(word)
            if(i+wordLen<tableLen):
              table[i+wordLen] += table[i] 
          # print ("index="+str(i)+" "+  word)
          # print (table )         
  return table[tableLen-1]



print(countConstruct('purple',['purp','p','ur','le','purpl'])) #2
print(countConstruct("abcdef",["ab","abc","cd","def","abcd"])) #1
print(countConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"])) #0
print(countConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"])) #4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
  "e",
  "ee",
  "eee",
  "eeee",
  "eeeee",
  "eeeeee",
  "eeeeeee",
  ])) #0
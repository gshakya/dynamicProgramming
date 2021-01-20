def canConstruct(target : str, wordBank: [str]):
  tableLen = len(target)+1
  table = [False]*tableLen
  table[0]= True
  for i in range(tableLen):
    if(table[i]):
      for word in wordBank:
          if(target.find(word,i)==i):
            wordLen= len(word)
            if(i+wordLen<tableLen):
              table[i+wordLen]= True
          # print ("index="+str(i)+" "+  word)
          # print (table )
        
  return table[tableLen-1]



print(canConstruct("abcdef",["ab","abc","cd","def","abcd"])) #true
print(canConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"])) #false
print(canConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"])) #true
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
  "e",
  "ee",
  "eee",
  "eeee",
  "eeeee",
  "eeeeee",
  "eeeeeee",
  ])) #false
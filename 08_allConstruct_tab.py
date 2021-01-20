from pprint import pprint
def allConstruct(target : str, wordBank: [str]):
  tableLen = len(target)+1
  table = [[]for x in range(tableLen+1)]
  table[0]= [[]]
  for i in range(tableLen):
    if(len(table[i])>0):
      for word in wordBank:
          if(target.find(word,i)==i):
            wordLen= len(word)
            if(i+wordLen<tableLen):
              for match in table[i]:
                table[i+wordLen].append(match+[word])
          # print ("index="+str(i)+" "+  word)
          # print (table )         
  return table[tableLen-1]



pprint(allConstruct('purple',['purp','p','ur','le','purpl'])) #2
pprint(allConstruct("abcdef",["ab","abc","cd","def","abcd"])) #1
pprint(allConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"])) #0
pprint(allConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"])) #4
pprint(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
  "e",
  "ee",
  "eee",
  "eeee",
  "eeeee",
  "eeeeee",
  "eeeeeee",
  ])) #0 exponential 
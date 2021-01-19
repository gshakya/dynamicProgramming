from pprint import pprint
def allConstruct ( targetString : str, wordBank : [str], memo = None):
  if(memo==None):
    memo ={}
  if(targetString in memo):
    return memo[targetString]
  if (targetString==""):
    return [[]]
  result = []
  for word in wordBank:
    if(targetString.find(word)==0):
      suffix = targetString[len(word):]
      suffWays= allConstruct(suffix,wordBank,memo)
      for i in  range(len(suffWays)):        
        result.append([word]+ suffWays[i])
  memoCpy= result.copy() 
  memo[targetString]=memoCpy
  return result  

pprint(allConstruct('purple',['purp','p','ur','le','purpl'])) #2
pprint(allConstruct("abcdef",["ab","abc","cd","def","abcd"])) #true
pprint(allConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"])) #false
pprint(allConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"])) #true
pprint(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
  "e",
  "ee",
  "eee",
  "eeee",
  "eeeee",
  "eeeeee",
  "eeeeeee",
  ])) #false
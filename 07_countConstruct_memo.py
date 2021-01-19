def countConstruct ( targetString : str, wordBank : [str], memo = None):
  if(memo==None):
    memo ={}
  if (targetString==""):
    return 1
  if(targetString in memo):
    return memo[targetString]
  totalCount = 0
  for word in wordBank:
    if(targetString.find(word)==0):
      suffix = targetString[len(word):]
      totalCount += countConstruct(suffix,wordBank,memo)      
  memo[targetString] = totalCount
  return totalCount  
print(countConstruct('purple',['purp','p','ur','le','purpl'])) #2
print(countConstruct("abcdef",["ab","abc","cd","def","abcd"])) #true
print(countConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"])) #false
print(countConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"])) #true
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
  "e",
  "ee",
  "eee",
  "eeee",
  "eeeee",
  "eeeeee",
  "eeeeeee",
  ])) #false
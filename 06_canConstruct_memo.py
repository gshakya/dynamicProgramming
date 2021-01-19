def canConstruct ( targetString : str, wordBank : [str], memo = None):
  if(memo==None):
    memo ={}
  if (targetString==""):
    return True
  if(targetString in memo):
    return memo[targetString]
  for word in wordBank:
    if(targetString.find(word)==0):
      suffix = targetString[len(word):]
      if(canConstruct(suffix,wordBank,memo)):
        memo[targetString] = True
        return True
  memo[targetString] = False
  return False  

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
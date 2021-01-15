def canConstruct ( targetString : str, wordBank : [str]):
  if (targetString==""):
    return True
  for word in wordBank:
    if(targetString.find(word)==0):
      suffix = targetString[len(word):]
      if(canConstruct(suffix,wordBank)):
        return True
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
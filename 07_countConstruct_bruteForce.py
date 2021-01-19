def countConstruct ( targetString : str, wordBank : [str]):
  if (targetString==""):
    return 1
  count = 0
  for word in wordBank:
    if(targetString.find(word)==0):
      suffix = targetString[len(word):]
      count += countConstruct(suffix,wordBank)
  return count

print(countConstruct('purple',['purp','p','ur','le','purpl']))
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
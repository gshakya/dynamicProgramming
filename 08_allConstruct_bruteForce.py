from pprint import pprint
def allConstruct ( targetString : str, wordBank : [str]):
  if (targetString==""):
    return [[]]
  result = []
  for word in wordBank:
    if(targetString.find(word)==0):
      suffix = targetString[len(word):]
      suffWays= allConstruct(suffix,wordBank)
      for i in  range(len(suffWays)):        
        result.append([word]+suffWays[i]) 
  return result

pprint(allConstruct('purple',['purp','p','ur','le','purpl']))
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
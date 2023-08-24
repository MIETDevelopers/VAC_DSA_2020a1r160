import re
def isValid(s):
  Pattern = re.compile("^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2}[.]\w{2}$")
  return Pattern.match(s)
s = input()
if (isValid(s)):
  print ("Valid Number")  
else :
  print ("Invalid Number")


#   Convert all atring stored in list to upper case using map & lambda
list = ['cat', 'rat', 'bat']
upperlist = list(map(lambda x : x.upper(), list))
print(upperlist)
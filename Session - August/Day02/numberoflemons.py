"""
a temple has 3 gods
each god has to be offered 7 lemons
once you enter the lemon ---  you check how many lemons you have
(if you have less lemons- --- buy lemons)
if you have more lemons --- reduce some
if you have 21 lemons --- you have sufficient 
if negative value --- no lemons

without control or conditional statements 

"""

lemon =  int(input("Enter the number of lemons you have"))

message = ""

if lemon < 21 and lemon > 0:
    message = "you need to buy " + str(21 - lemon) + " more lemons"
elif lemon > 21:
    message = "you have " + str(lemon - 21) + " more lemons"
elif lemon == 21:
    message = "you have sufficient lemons"
else:
    message = "invalid input" 
print(message)
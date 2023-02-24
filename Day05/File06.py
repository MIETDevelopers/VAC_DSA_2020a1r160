#Jump search in python
import math
lis = [1,2,3,5,8,17,18,19,20]
n = 8
gap = math.sqrt(len(lis))
count = 0
left = 0
while(lis[int(min(gap, len(lis)-1))]< n):
    left = gap
    gap = gap+math.sqrt(len(lis))
    if (left>=len(lis)):
        break
    while(lis[int(left)]<n):
        left = left+1
        
        if(left == min(gap, len(lis))):
            break
if(lis[int(left)]==n):
    print(int(left))
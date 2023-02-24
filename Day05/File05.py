#Interpolation Search
def InterpolationSearch(lis,l,h,n):
    if l<=h and n>=lis[l] and n<=lis[h]:
        pos = (l+h//(lis[h]-lis[l])*(n-lis[l]))
        #print(pos)
        if lis[pos]==n:
            return pos
        
        if lis[pos]<n:
            return InterpolationSearch(lis, pos+1, h, n)
        if lis[pos]>n:
            return InterpolationSearch(lis,l,pos-1,n)
        
    else:
        return 'Not found'
lis=[2,4,6,8,9,10,19,20,22]
print(InterpolationSearch(lis,0,len(lis)-1,7))
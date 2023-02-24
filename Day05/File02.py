# Binary search in python.
class BinarySearch:
    def searchMethod(self, lst, low, high, keyValue):
        self.lst = sorted(lst)
        if high >= low:
            mid = low+(high-1)//2
            if lst[mid] == keyValue:
                return mid
            elif lst[mid] > keyValue:
                return self.searchMethod(lst, low, mid-1, keyValue)
            else:
                return self.searchMethod(lst, mid+1, high, keyValue)
        else:
            return 'Not found'
lis = [14,2,3,7,9,10,12,15]
n = 12
obj = BinarySearch()
print(obj.searchMethod(lis, 0, len(lis)-1, n))
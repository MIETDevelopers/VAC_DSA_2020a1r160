# Linear search in python.
lst = [10,12,8,9,0,19,81,7,21,11,13]
class LinearSearch:
    def search(self, lst, keyValue):
        for i in range(len(lst)):
            if lst[i] == keyValue:
                return i
        return 'Not Found'

obj = LinearSearch()
print(obj.search(lst, 81))
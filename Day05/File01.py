# Linear search in python.
lst = [5, 4, 3, 2, 11, 7, 9, 12]
class LinearSearch:
    def search(self, lst, keyValue):
        for i in range(len(lst)):
            if lst[i] == keyValue:
                return i
        return 'Not Found'

obj = LinearSearch()
print(obj.search(lst, 1))
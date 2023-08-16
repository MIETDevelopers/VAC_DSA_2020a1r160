#Convert list into dictionary
my_list1 = ['apple', 'mango', 'grapes']
my_dict = {item: len(item) for item in my_list1}
print(my_dict)
#Washing machine problem
def count_steps(lst):
    lst_sum = sum(lst)
    lst_len = len(lst)
    val = lst_sum // lst_len
    new_lst = [val] * lst_len
    steps = 0
    while lst != new_lst:
        max_idx = lst.index(max(lst))
        min_idx = lst.index(min(lst))
        lst[max_idx] -= 1
        lst[min_idx] += 1
        steps += 1
    return new_lst, steps

list1 = [3, 1, 4, 8]
print("Original List:", list1)
new_list, steps = count_steps(list1)
print("New List:", new_list)
print("Steps:", steps)
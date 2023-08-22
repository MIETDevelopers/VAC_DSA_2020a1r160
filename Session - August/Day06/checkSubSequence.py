def is_subsequence(str1, str2):
    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
        j += 1
    return i == len(str1)

input_str1 = input()
input_str2 = input()

if is_subsequence(input_str1, input_str2) or is_subsequence(input_str2, input_str1):
    print("Yes")
else:
    print("No")

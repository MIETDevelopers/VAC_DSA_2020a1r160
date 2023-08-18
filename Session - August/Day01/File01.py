#print(chr(3172))
"""_summary_
    range for data types in C

signed int =  - 2147483648 to 214.....7
unsigned - 0 to 4294967295

ASCII Values
 a - z = 97 to 122
A- Z  = 65 to 90
0-9 = 48 to 57 
space bar = 32


chr() --- unicode to human understandable 
ord() --- human understandable to unicode


LCS - Longest Common Subsequences

* the characters is a sub sequence may or may not be consecutive as in the parent sequence
* subsequence are in the same direction - whenever there is an intersection of characters, do not consider the character which 
is in the opposite direction

implement by using
- recursion
memorization
tabulation(dynamic programming)


algorithm for dynamic programming approach:

def miet (i, j):
    if(a[i] == b[j]):
        return 1+miet(i-1, j-1)
    else:
        return mx(miet(i-1, j), miet(i, j-1))



# algorithm for Recursion:
# def miet(i,j):
#     if(a[i] == '\0 || b[j] == '\0):
#         return 0
#     elif(a[i] == b[j]):
#         return 1+miet(i-1, j-1)
#     else:
#         return max(miet(i-1, j), miet(i, j-1))
#     """
    
    


#homework

# longest palindrome subsequence
# longest commmon substring


#backtracking algorithm

# def jobschedule(jobs, time, N):
#     maxval = 0

#     for i in range(N):
#         temp = {}
#         for j in range(N-1):
a = 4
print(str(21-a) + " Lemons needed " if a<21 else "suffecient lemons" )

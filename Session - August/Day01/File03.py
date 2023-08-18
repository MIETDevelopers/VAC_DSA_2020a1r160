# #Python program to implement LCS problem using tabulation
# def lcs_tabulation(X, Y):
#     m = len(X)
#     n = len(Y)
    
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
    
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if X[i - 1] == Y[j - 1]:
#                 dp[i][j] = 1 + dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
#     lcs_length = dp[m][n]
    
#     lcs = []
#     i, j = m, n
#     while i > 0 and j > 0:
#         if X[i - 1] == Y[j - 1]:
#             lcs.append(X[i - 1])
#             i -= 1
#             j -= 1
#         elif dp[i - 1][j] > dp[i][j - 1]:
#             i -= 1
#         else:
#             j -= 1
    
#     lcs.reverse()
#     return lcs_length, ''.join(lcs)

# MainString = input("Enter the main string: ")
# SubString = input("Enter the sub string: ")
# MainString = MainString.lower()
# SubString = SubString.lower()

# length, sequence = lcs_tabulation(MainString, SubString)
# print("Length of LCS:", length)
# print("The length of the longest common subsequence is: ", sequence)

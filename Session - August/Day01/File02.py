#Python program to implement LCS problem
MainString = input("Enter the main string: ")
SubString = input("Enter the sub string: ")
MainString = MainString.lower()
SubString = SubString.lower()
def LCS(i, j):
    if(i == -1 or j == -1):
        return 0
    elif(MainString[i] == SubString[j]):
        return 1+LCS(i-1, j-1)
    else:
        return max(LCS(i-1, j), LCS(i, j-1))
print("The length of the longest common subsequence is: ", LCS(len(MainString)-1, len(SubString)-1))
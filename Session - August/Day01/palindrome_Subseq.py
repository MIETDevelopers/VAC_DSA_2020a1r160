#Python program to implement LCS problem

def LCS(i, j):
    if(i == -1 or j == -1):
        return 0
    elif(MainString[i] == SubString[j]):
        return 1+LCS(i-1, j-1)
    else:
        return max(LCS(i-1, j), LCS(i, j-1))
    
def palindromesubseq(s):
    rev = s[::-1]
    return LCS(len(s)-1, len(rev)-1)
#print("The length of the longest common subsequence is: ", LCS(len(MainString)-1, len(SubString)-1))
MainString = input("Enter the main string: ")
SubString = input("Enter the sub string: ")
MainString = MainString.lower()
SubString = SubString.lower()

print("The longest palindrome subsequence length is: ", palindromesubseq(MainString))

#Program to represent Naive Pattern
def search(pat, txt):
    M = len(pat)
    N = len(txt)
    for i in range(N - M + 1):
        j = 0
        while(j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1
        if (j == M):
            print("Pattern found at index ", i)
text = input("Enter string: ")
pattern = input("Enter pattern: ")
search(pattern, text)
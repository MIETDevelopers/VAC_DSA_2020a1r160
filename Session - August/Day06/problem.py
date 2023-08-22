N = int(input())
S = list(input())
Cash = int(input())
A = int(input())
B = int(input())

def swap():
   global Cash
   Rs = S.copy()
   S[S.index('1')], S[''.join(S).rindex('0')] = S[''.join(S).rindex('0')], S[S.index('1')]
   if Rs == S:
       flip()
   else:
       Cash -= A

def flip():
   global Cash
   S[S.index('1')] = '0'
   Cash -= B

while Cash > A or Cash > B:
   if A < B and '0' in S:
       swap()
   else:
       flip()
print(int(''.join(S), 2))
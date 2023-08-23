"""
 reverse words only if ith and n-ith have same length on comparing
 
 
ip: hello hai check
op: kcehc hai olleh

ip: hello hai bye check
op: kcehc eyb iah olleh

ip: hello hai check bye
op: hello hai check bye

ip: hello hai bye chennai
op: hello yeb iah chennai

ip: hello chennai am in kashmir hotts
op: sttoh rimhsak ni ma iannehc olleh

ip: hello check
op: kcehc olleh

ip: hello
op: hello
"""

def swap_and_reverse(s):
    words = s.split(" ")
    n = len(words)-1
    for i in range(len(words) - 1):
        if len(words[i]) == len(words[n-i]):
            #print(words[i])
            #print(words[n-i])
            words[i], words[n-i] = words[n-i], words[i]
            words[i] = words[i][::-1]
            words[n - i] = words[n-i][::-1]
    return ' '.join(words)

while True:
    user_input = input("Enter a string (type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        break
    
    output = swap_and_reverse(user_input)
    print(f"Modified Output: {output}")

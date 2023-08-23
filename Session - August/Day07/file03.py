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

def reverse_words(s):
    words = s.split()
    equal_length_words = []
    
    i = 0
    while i < len(words):
        word = words[i]
        if i + 1 < len(words) and len(words[i + 1]) == len(word):
            equal_length_words.append(word)
            while i < len(words) and len(words[i]) == len(word):
                i += 1
        else:
            equal_length_words.append(word[::-1])
            i += 1
    
    return ' '.join(equal_length_words)

while True:
    user_input = input("Enter a string (type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        break
    
    output = reverse_words(user_input)
    print(f"Modified Output: {output}")

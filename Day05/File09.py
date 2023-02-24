#The first line of input contains the integer K(1<-K<-45) , the number of times Mirko pressed the button.

def count_letters(K):
    word = "A"  
    for i in range(K):
        new_word = ""
        for letter in word:
            if letter == "A":
                new_word += "B"
            else:
                new_word += "BA"
        word = new_word

    num_a = word.count("A")
    num_b = word.count("B")
    return num_a, num_b
n = int(input())
print(count_letters(n))
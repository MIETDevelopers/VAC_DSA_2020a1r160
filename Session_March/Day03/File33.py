"""
1. you are in exploration of a new language where you find a tribe & your task is to find and script 
what they are trying to communicate. They use a number language where
101 means A and 102 refers to B and so on
Please decipher the language & communicate with tribe
input is given in the format of string return the words framing a sentence
i/p='101 102 108 102, 111 123 119 101, 109 113 117 112'
o/p=Abhb 
"""
class NumberTranslator:
    def __init__(self):
        self.num_to_letter = {
            101: 'A',
            102: 'B',
            103: 'C',
            104: 'D',
            105: 'E',
        }
    
    def to_letters(self, num_string):
        letters = ''
        nums = num_string.split()
        for num in nums:
            if int(num) in self.num_to_letter:
                letters += self.num_to_letter[int(num)]
        return letters

translator = NumberTranslator()

num_string = '101 102 103'
letters = translator.to_letters(num_string)
print(letters)
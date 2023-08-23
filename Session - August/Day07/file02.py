"""
ip: apple, banana, cat, zebra, cinderella
    : abczc

output: yes its true acronym

ip: apple, angle, banana, zebra
    : abz

output: no its false acronym

ip: apple, angle, aloevera
    : aa

output: no its false acronym
    """

def is_acronym(word_list, acronym):
    formed_acronym = ''.join(word[0] for word in word_list)
    return formed_acronym == acronym

word_list = input("Enter a list of words (comma separated): ").split(", ")
word_list = [word.lower() for word in word_list]

acronym = input("Enter the acronym: ")

if is_acronym(word_list, acronym):
    print("Yes its true - acronym")
else:
    print("No its false - not acronym")
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

word_list = input("Enter a list of words separated by commas: ").split(", ")
acronym = input("Enter the acronym to check: ")

if is_acronym(word_list, acronym):
    print("Yes, it is an acronym.")
else:
    print("No, it is not an acronym.")
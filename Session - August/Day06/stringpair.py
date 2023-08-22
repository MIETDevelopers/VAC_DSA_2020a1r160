def num_vowels(text):
    vowels = "AEIOUaeiou"
    return sum(1 for char in text if char in vowels)

def convert_to_textual(digits):
    num_to_text = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    return [num_to_text[digit] for digit in digits]

def find_pairs_with_sum(digits, target_sum):
    textual_representations = convert_to_textual(digits)
    pairs_count = 0

    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            sum_vowels = num_vowels(textual_representations[i]) + num_vowels(textual_representations[j])
            if sum_vowels == target_sum:
                pairs_count += 1

    return pairs_count

# Example usage
digit_list = input("Enter a list of digits (without spaces): ")
target_digit = int(input("Enter the target digit: "))

pairs_count = find_pairs_with_sum(digit_list, target_digit)
print(f"Total number of pairs with a sum of {target_digit} vowel count: {pairs_count}")
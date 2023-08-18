def check_neon(num):
    squared = num ** 2
    digit_sum = sum(int(digit) for digit in str(squared))
    if(digit_sum == num):
        return 1 
    return 0

def neon_num():
    start = 0
    stop = 100
    for n in range(start, stop+1):
        if (check_neon(n)):
            print(n)

neon_num()
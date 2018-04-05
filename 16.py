"""
very easy in path, could be hard in c/c++
"""
def get_sum_digit():
    digits = str(2 ** 1000)
    sum = 0
    for digit in digits:
        sum += int(digit)
    return sum

if __name__ == '__main__':
    print get_sum_digit()

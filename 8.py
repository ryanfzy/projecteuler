def product(digits):
    product = 1
    for digit in digits:
        product *= digit
    return product

def find_largest_set(digits):
    largest_set = []
    current_set = []
    largest_product = 0
    for ch_digit in digits:
        digit = int(ch_digit)
        if len(largest_set) < 13:
            current_set.append(digit)
            if len(current_set) == 13:
                largest_product = product(current_set) 
                largest_set = current_set
        else:
            current_set = current_set[1:]
            current_set.append(digit)
            current_product = product(current_set)
            if current_product > largest_product:
                largest_set = current_set
                largest_product = current_product
    print largest_set
    return largest_product

if __name__ == '__main__':
    with open('8.txt') as f:
        str_digits = ''
        for line in f.readlines():
            str_digits += line.strip()
        print find_largest_set(str_digits)


import prime
"""
the answer is 76576500
get_first_triangle_number() is slow
get_first_triangle_number2() is much faster
"""
def _get_next_triangle_number():
    num = 0
    iteration = 0
    while True:
        iteration += 1
        num += iteration
        yield num

def _get_divisor_count(num):
    count = 1
    largest = 3
    for i in range(2, num):
        if i >= largest:
            break
        if num % i == 0:
            largest = num / i
            count += 2
    return count

def get_first_triangle_number():
    num_divisors = 0
    for num in _get_next_triangle_number():
        divisors_length = _get_divisor_count(num)
        if divisors_length > num_divisors:
            num_divisors = divisors_length
            print str(num) + ':' + str(divisors_length)
        if divisors_length >= 500:
            return num
    return 0

def _get_divisor_count2(factors):
    count_dict = {}
    for factor in factors:
        if factor in count_dict:
            count_dict[factor] += 1
        else:
            count_dict[factor] = 1
    count = 1
    for value in count_dict.values():
        value = value + 1
        count *= value
    return count - 1

def get_first_triangle_number2():
    largest = 0
    for num in _get_next_triangle_number():
        factors = prime.get_factorisation(num)
        count = _get_divisor_count2(factors)
        if count > largest:
            print str(num) + ':' + str(count)
            largest = count
        if largest >= 500:
            return num
    return 0

if __name__ == '__main__':
    print get_first_triangle_number2()


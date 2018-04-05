def get_sum_proper_divisors(num):
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors

def is_abundant(num):
    sum_divisors = 0
    for i in range(num-1, 0, -1):
        if num % i == 0:
            sum_divisors += i
        if sum_divisors > num:
            return True
    return sum_divisors > num

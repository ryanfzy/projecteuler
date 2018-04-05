"""
this is suprisely not slow
"""

def _get_sum_proper_divisors(num):
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors

def get_sum_amicables(num):
    amicables = []
    for i in range(1, num):
        a = _get_sum_proper_divisors(i)
        if a > i:
            b = _get_sum_proper_divisors(a)
            if b == i:
                amicables.append(i)
                amicables.append(a)
    return sum(amicables)

if __name__ == '__main__':
    print get_sum_amicables(10000)


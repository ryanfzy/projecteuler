import shared
import timer

ABUNDANTS = []

def _is_sum_of_2_abundants(num):
    global ABUNDANTS
    if shared.get_sum_proper_divisors(num) > num:
        ABUNDANTS.append(num)
    for abundant in ABUNDANTS:
        if num - abundant in ABUNDANTS:
            return True
    return False

def get_sum():
    the_sum = 0
    for n in range(1, 28124):
        if not _is_sum_of_2_abundants(n):
            the_sum += n
    return the_sum

if __name__ == '__main__':
    atimer = timer.Timer()
    atimer.start()
    print get_sum()
    print atimer.how_long()


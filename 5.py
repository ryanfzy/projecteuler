import prime

def _get_factors(dst, src):
    ret = []
    dst_cpy = dst[:]
    for factor in src:
        if factor in dst_cpy:
            dst_cpy.remove(factor)
        else:
            ret.append(factor)
    return ret


def smallest_multiple():
    factors = []
    nums = range(1, 20)
    for num in nums:
        prime_factors = prime.get_prime_factors(num)
        print prime_factors
        factors.extend(_get_factors(factors, prime_factors))
        factors.sort()
    total = 1
    for factor in factors:
        total *= factor
    return 'TOTAL: ' + str(total)

if __name__ == '__main__':
    print smallest_multiple()


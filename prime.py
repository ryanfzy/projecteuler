class Primes:
    _primes = []
    
    def __init__(self):
        self._pos = 0

    def __iter__(self):
        return self

    def next(self):
        if self._pos < len(Primes._primes):
            next_prime = Primes._primes[self._pos]
            self._pos += 1
            return next_prime
        if len(Primes._primes) > 0:
            self._add_prime(Primes._primes[len(Primes._primes)-1])
        else:
            self._add_prime(0)
        return self.next()

    def _add_prime(self, start):
        num = start + 1
        while True:
            found_prime = True
            for prime in Primes._primes:
                if prime > 1 and num % prime == 0:
                    found_prime = False
                    break
            if found_prime:
                Primes._primes.append(num)
                break
            num += 1

def get_prime_factors(max):
    factors = []
    remain = max
    if max >= 1:
        factors.append(1)
    while remain > 1:
        for prime in Primes():
            if prime > 1 and remain % prime == 0:
                factors.append(prime)
                remain /= prime
                break
    return factors

def get_factorisation(num):
    factors = get_prime_factors(num)
    remain = num
    result = []
    while remain > 1:
        for factor in factors:
            if factor > 1 and remain % factor == 0:
                result.append(factor)
                remain /= factor
    result.sort()
    return result

def get_prime_generator():
    primes = []
    next_prime = 0
    while True:
        found_prime = True
        next_prime += 1
        if len(primes) > 0:
            for prime in primes:
                if prime > 1 and next_prime % prime == 0:
                    found_prime = False
                    break
        if found_prime:
            primes.append(next_prime)
            yield next_prime

def test_primes():
    num = 0
    for prime in Primes():
        print prime
        num += 1
        if num > 10:
            break
    num = 0
    for prime in Primes():
        print prime
        num += 1
        if num > 10:
            break

if __name__ == '__main__':
    test_primes()

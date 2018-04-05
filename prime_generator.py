def _num_generator(start, max):
    num = start
    while num < max:
        yield num
        num += 1

def _prime_generator(max):
    primes = []
    generator = _num_generator(2, max)
    for i in generator:
        found = False
        for prime in primes:
            if i % prime == 0:
                found = True
                break
        if not found:
            primes.append(i)
            yield i

def get(max):
    generator = _prime_generator(max)
    for prime in generator:
        if max % prime == 0:
            yield prime


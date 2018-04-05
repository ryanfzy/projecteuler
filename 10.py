import prime

def sum_of_primes():
    max = 2000000
    sum = 0
    for prime_number in prime.get_primes(10):
        sum += prime_number
    return sum

if __name__ == '__main__':
    print sum_of_primes()

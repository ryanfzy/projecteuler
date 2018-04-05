import prime_factor_generator

def largest_prime():
    max = 600851475143
    #generator = prime_factor_generator(max)
    generator = prime_factor_generator.get(max)
    for prime_factor in generator:
        print prime_factor

if __name__ == '__main__':
    largest_prime()

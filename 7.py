import prime

def get_10001st_prime():
    generator = prime.get_prime_generator()
    for i in range(10002):
        print generator.next()

if __name__ == '__main__':
    get_10001st_prime()

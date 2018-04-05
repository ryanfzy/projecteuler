def _square(n):
    return n * n

def find_triplet():
    a_max = 332 + 1
    for a in range(1, a_max):
        b_max = (1000 - a) / 2
        for b in range(a+1, b_max):
            square_c = _square(a) + _square(b)
            c = 1000 - a - b
            if square_c == _square(c):
                print [a, b, c]
                return a * b * c
    return []

if __name__ == '__main__':
    print find_triplet()


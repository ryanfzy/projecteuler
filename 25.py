F1 = 1
F2 = 1
INDEX = 2

def _get_next_fib():
    global F1
    global F2
    F1, F2 = F2, F1 + F2
    return F2

def get_index():
    global INDEX
    while True:
        fib = _get_next_fib()
        INDEX += 1
        if len(str(fib)) >= 1000:
            return INDEX


if __name__ == '__main__':
    print get_index()

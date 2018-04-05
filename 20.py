def get_sum():
    factorial = 1
    total = 0
    for n in range(100, 0, -1):
        factorial *= n 
    print 'factorial: ' + str(factorial)
    for digit in str(factorial):
        total += int(digit)
    return total

if __name__ == '__main__':
    print get_sum()


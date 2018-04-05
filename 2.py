def fib_generator(max):
    num1 = 0
    num2 = 1
    while num2 < max:
        num3 = num1 + num2
        if num3 > max:
            raise StopIteration
        yield num3
        num1 = num2
        num2 = num3

def _is_even(num):
    last_digit = int(str(num)[-1])
    return last_digit % 2 == 0

def sum():
    generator = fib_generator(4000000)
    sum = 0
    for num in generator:
        if _is_even(num):
            sum += num
    return sum

if __name__ == '__main__':
    print sum()

def _is_palindromic(num):
    num_str = str(num)
    for i in range(len(num_str)/2):
        if num_str[i] != num_str[len(num_str)-i-1]:
            return False
    return True

def largest_palindromic():
    largest = 0
    for i in range(1000):
        for j in range(1000):
            num = i * j
            if _is_palindromic(num) and num > largest:
                largest = num
    return largest

if __name__ == '__main__':
    print largest_palindromic()

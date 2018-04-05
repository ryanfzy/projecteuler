def _get_diff():
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, 101):
        square_of_sum += i
        sum_of_squares = sum_of_squares + i * i
    print 'sum: ' + str(square_of_sum)
    square_of_sum = square_of_sum * square_of_sum
    print 'square of sum: ' + str(square_of_sum)
    print 'sum of squares: ' + str(sum_of_squares)
    return square_of_sum - sum_of_squares

if __name__ == '__main__':
    print _get_diff()

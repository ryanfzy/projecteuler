def sum3and5():
    MAX = 1000
    sum = 0
    start3 = 0
    start5 = 0
    while True:
        if start3 > MAX and start5 >= MAX:
            break
        if start5 < MAX:
            start5 += 5
        while start3 < MAX and start3 < start5:
            #print '3:' + str(start3)
            sum += start3
            start3 += 3
        if start3 != start5 and start5 < MAX:
            #print '5:' + str(start5)
            sum += start5
    return sum

if __name__ == '__main__':
    print sum3and5()


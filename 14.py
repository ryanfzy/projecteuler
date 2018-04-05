#MILLION = 20
MILLION = 1000000
CHAIN = []
CHAIN_DICT = {}
NUMBER = 0

"""
this tries to find the answer reversely, but it is not working
or may be it is impossible to find the answer reversely
"""
def find_start(start, next_start, chain, stop):
    global MILLION
    global CHAIN
    if start >= MILLION and next_start >= MILLION and stop:
        for last in range(len(chain)-1, -1, -1):
            if last < MILLION:
                chain = chain[:last-1]
                break
        if len(chain) >= len(CHAIN):
            CHAIN = chain
        #print 'start:' + str(start) + ';next_start:' + str(next_start)
        return
    stop = start >= MILLION and next_start >= MILLION
    start = next_start
    current_chain = chain[:]

    current_chain.append(start)
    if start > 4 and (start - 1) % 3 == 0:
        next_start = (start - 1) / 3
        if next_start % 2 == 1:
            find_start(start, next_start, current_chain, stop)

    next_start = start * 2
    find_start(start, next_start, current_chain, stop)

def get_collatz_seq(num):
    if num in CHAIN_DICT:
        return CHAIN_DICT[num]
    else:
        count = 1
        if num <= 1:
            return count
        if num % 2 == 0:
            next_num = num / 2
            count += get_collatz_seq(next_num)
        else:
            next_num = num * 3 + 1
            count += get_collatz_seq(next_num)
        return count

if __name__ == '__main__':
    """
    find_start(1, 1, [], False)
    print 'chain:' + str(CHAIN)
    """
    for i in range(MILLION+1):
        count = get_collatz_seq(i)
        CHAIN_DICT[i] = count
        print str(i) + ':' + str(count)
    largest = 0
    for i in CHAIN_DICT:
        if largest < CHAIN_DICT[i]:
            largest = CHAIN_DICT[i]
            NUMBER = i
    print str(NUMBER) + ':' + str(largest)


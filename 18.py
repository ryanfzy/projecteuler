ROWS = []
MAX_SUM = 0
TRIES = 0
def get_max(row, col, max_sum):
    global ROWS
    global TRIES
    global MAX_SUM
    max_sum += ROWS[row][col]
    if row >= len(ROWS)-1:
        TRIES += 1
        if max_sum > MAX_SUM:
            MAX_SUM = max_sum
    else:
        get_max(row+1, col, max_sum)
        get_max(row+1, col+1, max_sum)
    
if __name__ == '__main__':
    with open('18.txt') as f:
        for line in f.readlines():
            ROWS.append([int(num) for num in line.strip().split()])
    for row in ROWS:
        print row
    get_max(0, 0, 0)
    print MAX_SUM
    print TRIES

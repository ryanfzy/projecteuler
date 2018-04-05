WORDS = {}
WORDS[0] = 0
WORDS[1] = len('one')
WORDS[2] = len('two')
WORDS[3] = len('three')
WORDS[4] = len('four')
WORDS[5] = len('five')
WORDS[6] = len('six')
WORDS[7] = len('seven')
WORDS[8] = len('eight')
WORDS[9] = len('nine')
WORDS[10] = len('ten')
WORDS[11] = len('eleven')
WORDS[12] = len('twelve')
WORDS[13] = len('thirteen')
WORDS[14] = len('fourteen')
WORDS[15] = len('fifteen')
WORDS[16] = len('sixteen')
WORDS[17] = len('seventeen')
WORDS[18] = len('eighteen')
WORDS[19] = len('nineteen')
WORDS[20] = len('twenty')
WORDS[30] = len('thirty')
WORDS[40] = len('forty')
WORDS[50] = len('fifty')
WORDS[60] = len('sixty')
WORDS[70] = len('seventy')
WORDS[80] = len('eighty')
WORDS[90] = len('ninety')

def get_count(num):
    global WORDS
    if num in WORDS:
        return WORDS[num]
    else:
        if num >= 1000:
            remainder = num % 1000
            first_digit = (num - remainder) / 1000
            count = get_count(first_digit)
            count += len('thousand')
            if remainder > 0:
                count += len('and')
                count += get_count(remainder)
            WORDS[num] = count
            return count
        elif num >= 100:
            remainder = num % 100
            first_digit = (num - remainder) / 100
            count = get_count(first_digit)
            count += len('hundred')
            if remainder > 0:
                count += len('and')
                count += get_count(remainder)
            WORDS[num] = count;
            return count
        else:
            remainder = num % 10
            count = get_count(num - remainder)
            if remainder > 0:
                count += get_count(remainder)
            WORDS[num] = count;
            return count

def get_sum_counts():
    sum = 0
    for i in range(1, 1001):
        sum += get_count(i)
    return sum

if __name__ == '__main__':
    print get_sum_counts()

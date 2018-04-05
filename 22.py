def _get_score(name):
    score = 0
    for ch in name:
        score = score + ord(ch) - ord('A') + 1
    return score

def get_name_score():
    with open('p022_names.txt') as f:
        names = ''
        for line in f.readlines():
            names += line
        names = [name.strip("'\"") for name in names.split(',')]
        names.sort()
        sum_score = 0
        for i in range(len(names)):
            sum_score += (_get_score(names[i]) * (i+1))
        return sum_score

if __name__ == '__main__':
    print get_name_score()


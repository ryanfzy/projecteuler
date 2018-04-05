"""
the anwser: 2783915460
"""
NTH = 0
MAX_TH = 1000000

def _shift(digits, start, end):
    copy = digits[:]
    for i in range(start, end):
        copy[i+1] = digits[i]
    copy[start] = digits[end]
    return copy

def _get_nth_perm(digits, pos):
    global NTH
    global MAX_TH
    for idx in range(pos, len(digits)):
        copy = digits[:]
        if idx > pos:
            NTH += 1
            copy = _shift(digits, pos, idx)
            print str(NTH)+':'+str(copy)
            if NTH == MAX_TH:
                quit()
        _get_nth_perm(copy, pos+1)

def get_nth_perm():
    global NTH
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print digits
    NTH = 1
    _get_nth_perm(digits, 0)

if __name__ == '__main__':
    get_nth_perm()

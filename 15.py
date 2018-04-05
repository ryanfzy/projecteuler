import math

"""
both find_path and find_path2 works
but find_path2 is fast because it has the power of math
"""
PATH_DICT = {}
def find_path(start, end, path):
    global PATH_DICT
    #global PATH
    if str(start) in PATH_DICT:
        return PATH_DICT[str(start)]
    if start[0] == end[0] and start[1] == end[1]:
        return path + 1
    if start[1] < end[1]:
        new_start = [start[0], start[1]+1]
        new_path = find_path(new_start, end, 0)
        print 'start:' + str(new_start) + ';' + str(new_path)
        PATH_DICT[str(new_start)] = new_path
        path += new_path
    if start[0] < end[0]:
        new_start = [start[0]+1, start[1]]
        new_path = find_path([start[0]+1, start[1]], end, 0)
        print 'start:' + str(new_start) + ';' + str(new_path)
        PATH_DICT[str(new_start)] = new_path
        path += new_path
    return path

def find_path2(a, b):
    return math.factorial(a+b) / (math.factorial(a) * math.factorial(b))

if __name__ == '__main__':
    print find_path2(20, 20)

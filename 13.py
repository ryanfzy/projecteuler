"""
this is easy because python can handle very large number
for other langauges that doesn't have this kind of native support (e.g. c/cpp)
  could be difficult
"""
def sum():
    result = 0
    with open('13.txt') as f:
        for line in f.readlines():
            num = int(line.strip())
            result += num
    return result

if __name__ == '__main__':
    print sum()

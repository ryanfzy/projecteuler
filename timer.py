import time

class Timer:
    def __init__(self):
        self._start = 0

    def start(self):
        self._start = time.time()

    def reset(self):
        self._start = time.time()

    def how_long(self):
        return time.time() - self._start

if __name__ == '__main__':
    print "(Timer) Run Tests:"
    timer = Timer()
    timer.start()
    time.sleep(2)
    print timer.how_long()

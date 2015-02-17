# iteration sample

from itertools import imap

class CountDown(object):
    """docstring for CountDown"""
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def next(self):
        if self.count <= 0:
            raise StopIteration

        r = self.count
        self.count -= 1
        return r


if __name__ == '__main__':


    print imap(lambda x: x, CountDown(10)).next()

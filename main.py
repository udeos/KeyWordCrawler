from time import time

from core import ThreadCallbackHandler, ProcessCallbackHandler


if __name__ == '__main__':

    def callback(response):
        print(response)

    t = time()
    tch = ThreadCallbackHandler(callback, 10)
    tch.handle(['http://ping.eu/'] * 10)
    print(time() - t)

    def parse_m1():
        pass

    def parse_m2():
        pass

    pch = ProcessCallbackHandler(2)


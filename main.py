from time import time

from core import ThreadProcessor


if __name__ == '__main__':

    def callback(response):
        print(response)

    t = time()
    rp = ThreadProcessor(callback, 3)
    rp.process(['http://ping.eu/'] * 100)
    print(time() - t)

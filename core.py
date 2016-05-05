from queue import Queue
from threading import Thread
from http import client


class RequestProcessor:

    def __init__(self, callback, concurrency=1):
        self.callback = callback
        self.concurrency = concurrency
        self.queue = Queue(self.concurrency)
        self.daemons = []

    def process(self, urls):
        self.spawn_daemons()
        for url in urls:
            self.queue.put(url)
        self.queue.join()
        self.kill_daemons()

    def spawn_daemons(self):
        for i in range(self.concurrency):
            t = Thread(target=self.daemon_worker)
            t.daemon = True
            t.start()
            self.daemons.append(t)

    def kill_daemons(self):
        pass

    def daemon_worker(self):
        pass

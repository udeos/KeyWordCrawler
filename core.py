from queue import Queue
from threading import Thread


class ThreadProcessor:

    def __init__(self, callback, concurrency=1):
        self.callback = callback
        self.concurrency = concurrency
        self.queue = Queue(self.concurrency * 2)

    def process(self, items):
        self._spawn_daemons()
        for item in items:
            self.queue.put(item)
        self.queue.join()

    def _spawn_daemons(self):
        for i in range(self.concurrency):
            t = Thread(target=self.daemon_worker)
            t.daemon = True
            t.start()

    def daemon_worker(self):
        while True:
            item = self.queue.get()
            self.callback(item)
            self.queue.task_done()

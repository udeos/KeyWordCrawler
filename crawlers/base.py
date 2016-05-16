import threading
import time

from http import client
from queue import Queue
from collections import deque


class BaseCrawler:

    def __init__(self, settings):
        self.host = settings.HOST
        self.daemons = settings.DAEMONS_COUNT
        self.queue = Queue()
        self._spawn_daemons()
        self.last_requests = deque([time.time()], maxlen=settings.RPS)

    def _spawn_daemons(self):
        for _ in range(self.daemons):
            t = threading.Thread(target=self._daemon_worker)
            t.daemon = True
            t.start()

    def _daemon_worker(self):
        conn = client.HTTPSConnection(self.host)
        while True:
            current_time = time.time()
            if (current_time - self.last_requests[0]) < 1.:
                continue
            self.last_requests.append(current_time)
            item = self.queue.get()
            self.callback(item, conn)
            self.queue.task_done()

    def process(self, item):
        self.queue.put(item)

    def wait(self):
        self.queue.task_done()

    def callback(self, item, conn):
        raise NotImplementedError

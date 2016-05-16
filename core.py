from queue import Queue
import threading
import multiprocessing


class ThreadCallbackHandler:

    def __init__(self, callback, threads=1):
        self.callback = callback
        self.threads = threads
        self.queue = Queue(self.threads * 2)

    def handle(self, items):
        for i in range(self.threads):
            t = threading.Thread(target=self._daemon_worker)
            t.daemon = True
            t.start()
        for item in items:
            self.queue.put(item)
        # self.queue.join()

    def _daemon_worker(self):
        while True:
            item = self.queue.get()
            self.callback(item)
            self.queue.task_done()


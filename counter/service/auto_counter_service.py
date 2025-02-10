import threading
import time

class AutoCounterService:

    def __init__(self):
        self.__value = 0 # private
        self.start_background_thread()

    def inc(self):
        self.__value = self.__value + 1

    @property
    def value(self):
        return self.__value

    # background function in thread
    def background_task(self):
        print("run background_task")
        while True:
            time.sleep(1)
            self.inc()

    def start_background_thread(self):
        thread = threading.Thread(target=self.background_task, daemon=True)
        thread.start()

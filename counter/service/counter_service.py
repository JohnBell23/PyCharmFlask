class CounterService:

    counter = 0

    def increment(self):
        self.counter = self.counter + 1

    def read_counter(self):
        return self.counter

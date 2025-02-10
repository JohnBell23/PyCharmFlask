class CounterService:

    def __init__(self):
        self.__counter = 0

    def increment(self):
        self.__counter = self.__counter + 1

    @property
    def counter(self):
        return self.__counter

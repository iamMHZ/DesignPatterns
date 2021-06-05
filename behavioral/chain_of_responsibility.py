from abc import ABC


class Handler(ABC):

    def __init__(self, next_handler):
        self.__next_handler = next_handler

    @property
    def next_handler(self):
        return self.__next_handler

    @next_handler.setter
    def next_handler(self, next_handler):
        self.__next_handler = next_handler

    def handle(self, request, data):
        pass


class HandleAuthentication(Handler):

    def __init__(self, next_handler):
        super().__init__(next_handler)

    def set_next_handler(self, next_handler):
        self.__next_handler = next_handler

    def handle(self, request, data):
        pass


if __name__ == '__main__':
    pass

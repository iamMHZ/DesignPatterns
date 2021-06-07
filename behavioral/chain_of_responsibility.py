# TODO add anti-chain and docs
# TODO add descriptions
# TODO add doc string

from abc import ABC


class Handler(ABC):

    def __init__(self, next_handler=None):
        self.__next_handler = next_handler

    def add_next_handler(self, next_handler):
        self.__next_handler = next_handler
        return next_handler

    @property
    def next_handler(self):
        return self.__next_handler

    def handle(self, request):
        pass


class AuthenticationHandler(Handler):

    def __init__(self, next_handler):
        super().__init__(next_handler)

    def handle(self, request):
        print('Handling Authentication')


class DataValidationHandler(Handler):

    def __init__(self, next_handler):
        super().__init__(next_handler)

    def handle(self, request):
        print("Handling data validation  ")


if __name__ == '__main__':
    pass

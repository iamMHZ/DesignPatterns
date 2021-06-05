# TODO add anti-chain and docs

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

    def handle(self, request, data):
        print('Handling Authentication')

        # if self.next_handler is not None:
        #     self.next_handler.handle(request, data)
        #
        # else:
        #     print('Done')


if __name__ == '__main__':
    pass

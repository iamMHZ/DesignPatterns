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


class User:

    def __init__(self, username, password):
        self.__user_name = username



class Request:
    def __init__(self, user, data):
        self.__user = user
        self.__data = data

    @property
    def data(self):
        return self.__data

    @property
    def user(self):
        return self.__user



class AuthenticationHandler(Handler):

    def __init__(self, next_handler=None):
        super().__init__(next_handler)

    def handle(self, request):
        print('Handling Authentication')


class DataValidationHandler(Handler):

    def __init__(self, next_handler=None):
        super().__init__(next_handler)

    def handle(self, request):
        print("Handling data validation")


class UserPermissionHandler(Handler):

    def __init__(self, next_handler=None):
        super().__init__(next_handler)

    def handle(self, request):
        print('Handling Permissions')


if __name__ == '__main__':
    pass

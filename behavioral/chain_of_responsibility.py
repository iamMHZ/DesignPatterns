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

    def check_next(self, request):
        if self.__next_handler is not None:
            return self.__next_handler.handle(request)

        return False

    def handle(self, request):
        pass


class User:

    def __init__(self, username, password, role='simple_user'):
        self.__user_name = username
        self.__password = password
        self.__role = role

    @property
    def user_name(self):
        return self.__user_name

    @property
    def role(self):
        return self.__role


class Request:
    def __init__(self, user, data=None, request_type='GET'):
        self.__user = user
        self.__data = data
        self.__request_type = request_type

    @property
    def request_type(self):
        return self.__request_type

    @property
    def data(self):
        return self.__data

    @property
    def user(self):
        return self.__user


class PasswordAuthenticationHandler(Handler):

    def __init__(self, next_handler=None):
        super().__init__(next_handler)

    def handle(self, request):
        print('Handling Authentication')
        return self.check_next(request)


class DataValidationHandler(Handler):

    def __init__(self, next_handler=None):
        super().__init__(next_handler)

    def handle(self, request):
        print('Handling data validation')
        return self.check_next(request)


class UserPermissionHandler(Handler):

    def __init__(self, next_handler=None):
        super().__init__(next_handler)

    def handle(self, request):
        print('Handling Permissions')
        return self.check_next(request)


if __name__ == '__main__':
    user = User('iam_mhz', '12345')

    password_authentication = PasswordAuthenticationHandler()
    password_authentication. \
        add_next_handler(UserPermissionHandler()) \
        .add_next_handler(DataValidationHandler())

    password_authentication.handle(request=Request(user))

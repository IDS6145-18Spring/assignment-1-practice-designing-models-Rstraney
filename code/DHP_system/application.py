
from User import User


class Application:
    ''' A general application class '''

    def __init__(self, f, b):
        '''Intializes the application'''
        self.front_end = f
        self.back_end = b


    def __str__(self):
        '''Welcome Page'''
        return "Hello, {}.  Welcome to the Dogs Helping Pets Network!".format(User.name)

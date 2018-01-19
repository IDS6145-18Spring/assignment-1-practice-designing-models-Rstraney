from Application import Application
from User import User

class TrainingResources(Application):
    ''' A general Training Resources class '''

    def __init__(self, id):
        '''Intializes the Training Resources'''
        self.id = id

    def check_trainer_status(self):
        '''Message for Training Resources'''
        if User.lost_pet_status == True:
            print("Hey {}, you have access to Training Resources!".format(User.name))
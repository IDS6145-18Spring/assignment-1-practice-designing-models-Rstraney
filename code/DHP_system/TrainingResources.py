from application import application
from user import user

class TrainingResources(application):
    ''' A general Training Resources class '''

    def __init__(self, id):
        '''Intializes the Training Resources'''
        self.id = id

    def check_trainer_status(self):
        '''Message for Training Resources'''
        if user.lost_pet_status = True
            print("You have access to Training Resources!")
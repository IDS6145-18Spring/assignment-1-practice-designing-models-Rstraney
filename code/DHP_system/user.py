class user:
    ''' A general user class '''

    def __init__(self, id, n, pw, e, l, t):
        '''Intializes the vegtable'''
        self.id = id
        self.name = n
        self.password = pw
        self.email = e
        self.lost_pet_status = False
        self.trainer_status = False


    def __str__(self):
        '''Welcome Page'''
        return "Hello, {}.  Welcome to the Dogs Helping Pets Network!".format(
            self.name)


    def lost_pet_request(self):
        '''Function for Lost Pet Post - default FALSE'''
        self.lost_pet_status = True

    def trainer_access(self):
        '''Function for Trainer Access to Modules - default FALSE'''
        self.trainer_status = True

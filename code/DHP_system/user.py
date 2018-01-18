class user:
    ''' A general user class '''

    def __init__(self, id, n, pw, e, l, t):
        '''Intializes the vegtable'''
        self.id = id
        self.name = n
        self.password = pw
        self.email = e
        self.lost_pet_status = l
        self.trainer_status = t


    def __str__(self):
        '''Welcome Page'''
        return "Hello, {}.  Welcome to the Dogs Helping Pets Network!".format(
            self.name)


    def lost_pet_request(self):
        '''Function for Lost Pet Post'''
        raise NotImplementedError("Please Implement the Grow method!")
        #This containts a check to make sure subclasses implement this.
        return None


    def trainer_access(self):
        '''Function for Trainer Access to Modules'''
        raise NotImplementedError("Please Implement the Volume method!")
        #This containts a check to make sure subclasses implement this.
        return None

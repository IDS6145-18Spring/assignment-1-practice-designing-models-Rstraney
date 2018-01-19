from training_resources import training_resources

class ModuleB(training_resources):
    ''' Module_A '''

    def __init__(self, id, g):
        '''Intializes Module A'''
        self.id = id
        self.modB_grade = g

    def __str__(self):
        '''Module Content'''
        return "This is the content of Module A."


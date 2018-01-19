import math
from TrainingResources import TrainingResources
from TopicA1 import TopicA1

class ModuleA(TrainingResources):
    ''' Module_A '''

    def __init__(self, id, g):
        '''Intializes Module A'''
        self.id = id
        self.modA_grade = g

    def Calc_ModA_grade(self):
        '''The grade for Module A is the
        average score for all topics in the module'''
        return math.average(T1, T2)

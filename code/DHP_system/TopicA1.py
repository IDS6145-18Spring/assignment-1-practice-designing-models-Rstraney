from TrainingResources import TrainingResources

class TopicA1(TrainingResources):
    ''' TopicA1 '''

    def __init__(self, id, g):
        '''Intializes Module A'''
        self.id = id
        self.TopA1_grade = g

    def Calc_TopA1_grade(self):
        '''The grade for Module A is the sum of all correct questions in the quiz'''
        Q1 = 1
        Q2 = 1
        Q3 = 0
        Q4 = 0
        Q5 = 1

        TopA1_grade = sum(Q1, Q2, Q3, Q4, Q5)
        return TopA1_grade

from TrainingResources import TrainingResources

class TopicB2(TrainingResources):
    ''' TopicB2 '''

    def __init__(self, id, g):
        '''Intializes Module A'''
        self.id = id
        self.TopB2_grade = g

    def Calc_TopB2_grade(self):
        '''The grade for Module A is the sum of all correct questions in the quiz'''
        Q1 = 1
        Q2 = 1
        Q3 = 0
        Q4 = 0
        Q5 = 1

        TopB2_grade = sum(Q1, Q2, Q3, Q4, Q5)
        return TopB2_grade

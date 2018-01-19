from TrainingResources import TrainingResources

class TopicB1(TrainingResources):
    ''' TopicB1 '''

    def __init__(self, id, g):
        '''Intializes Module A'''
        self.id = id
        self.TopB1_grade = g

    def Calc_TopB1_grade(self):
        '''The grade for Module A is the sum of all correct questions in the quiz'''
        Q1 = 1
        Q2 = 1
        Q3 = 0
        Q4 = 0
        Q5 = 1

        TopB1_grade = sum(Q1, Q2, Q3, Q4, Q5)
        return TopB1_grade

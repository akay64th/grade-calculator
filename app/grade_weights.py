

class GradeWeights:
    """
    Specifies the weights assigned to each grade
    catefory for ENPM611.
    """
    
    def __init__(self) -> None:
        self.quizzes = 0.1
        self.midterm = 0.2
        self.project = 0.4
        self.final = 0.3


class ProjectHeavyWeights(GradeWeights):
    """
    Alternate grading scheme that puts more weight on the
    project and less on quizzes.
    """

    def __init__(self) -> None:
        self.quizzes = 0.05
        self.midterm = 0.15
        self.project = 0.6
        self.final = 0.2
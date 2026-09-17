
# DESIGN REVIEW
# If a future grading scheme replaced the single final exam with two smaller
# exams, several things in the current design would need to change:
#   1. Grades class: would need two new fields (e.g. final_1, final_2) instead
#      of (or alongside) `final`.
#   2. calculate_course_percentage: the None-check would need to check both
#      new fields, and final_part would need to average the two exams before
#      multiplying by weights.final, similar to how quizzes are averaged now.
#   3. calculate_optimistic_course_percentage: the same two None-checks and
#      1.0 fallbacks would need to be duplicated for the new final fields.
#   4. GradeWeights / ProjectHeavyWeights: no change needed, since the overall
#      weight assigned to "final" as a category would stay the same, it would
#      just be computed from an average of two scores instead of one.
# This is a moderate amount of change: three of the four files need edits,
# and the same None-check/average/fallback pattern used for quizzes would
# need to be copy-pasted for finals, which is a sign the codebase could
# benefit from a shared helper function to reduce duplication.

import copy

from grades import Grades
from grade_weights import GradeWeights

class GradeCalculator:
    """
    Calculates the overall course grade for ENPM611.
    """
    
    @staticmethod
    def calculate_course_percentage(grades:Grades, weights:GradeWeights) -> float:
        if grades.quiz_1 is None or grades.quiz_2 is None or grades.quiz_3 is None or grades.midterm is None or grades.project is None or grades.final is None:
            print("Can't calculate final grade without all assignments graded")
            return None
        else:
            quizzes_part = ((grades.quiz_1 + grades.quiz_2 + grades.quiz_3) / 3) * weights.quizzes
            midterm_part = grades.midterm * weights.midterm
            project_part = grades.project * weights.project
            final_part = grades.final * weights.final
            course_grade = quizzes_part + midterm_part + project_part + final_part
            return course_grade
        
    @staticmethod
    def calculate_optimistic_course_percentage(grades:Grades, weights:GradeWeights) -> float:
        optimistic_grades:Grades = copy.copy(grades)
        
        if optimistic_grades.quiz_1 is None:
            optimistic_grades.quiz_1 = 1
        if optimistic_grades.quiz_2 is None:
            optimistic_grades.quiz_2 = 1
        if optimistic_grades.quiz_3 is None:
            optimistic_grades.quiz_3 = 1
        if optimistic_grades.midterm is None:
            optimistic_grades.midterm = 1
        if optimistic_grades.project is None:
            optimistic_grades.project = 1
        if optimistic_grades.final is None:
            optimistic_grades.final = 1
        
        return GradeCalculator.calculate_course_percentage(optimistic_grades, weights)
        
    @staticmethod
    def calculate_letter_grade(percentage_grade:float) -> str:
        if percentage_grade is None:
            return None
        
        if percentage_grade >= 0.97:
            return 'A+'
        elif percentage_grade >= 0.93:
            return 'A'
        elif percentage_grade >= 0.90:
            return 'A-'
        elif percentage_grade >= 0.87:
            return 'B+'
        elif percentage_grade >= 0.83:
            return 'B'
        elif percentage_grade >= 0.80:
            return 'B-'
        elif percentage_grade >= 0.77:
            return 'C+'
        elif percentage_grade >= 0.73:
            return 'C'
        elif percentage_grade >= 0.70:
            return 'C-'
        elif percentage_grade >= 0.6:
            return 'D'
        else:
            return 'F'
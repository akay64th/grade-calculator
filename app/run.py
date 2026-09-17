

from grades import Grades
from grade_weights import GradeWeights, ProjectHeavyWeights
from grade_calculator import GradeCalculator

# This runs the grade calculation.

# Instatiate Grade and Weights objects
my_grades = Grades()
weights = GradeWeights()

# Prediction: with quiz_1=0.78 and all other grades None, the optimistic
# calculation should give 98.9% (an A), since all missing grades default to 100%.

# Set grades achieved so far
my_grades.quiz_1 = 0.82
my_grades.quiz_2 = 0.75
my_grades.quiz_3 = 0.85
my_grades.midterm = 0.88
my_grades.project = 0.91
my_grades.final = 0.79

# Bumping each grade category by +0.1 shows: quiz +0.5pts, midterm +2.0pts,
# final +3.0pts, project +4.0pts to the overall percentage. Project has the
# most impact because it carries the highest weight (40%) in GradeWeights.

# Print out the grades to console
print(my_grades)

# Calculate course grade based on the grades set above
percentage_grade = GradeCalculator.calculate_course_percentage(my_grades, weights)
if percentage_grade is None:
    print("Can't calculate overall course grade without all individual grades.")
else:
    letter_grade = GradeCalculator.calculate_letter_grade(percentage_grade)
    print(f'The letter grade with an overall {percentage_grade*100}% is {letter_grade}')

# Calculate the grade assuming that all assignmets not turned in yet, will be 100%
optimistic_percentage_grade = GradeCalculator.calculate_optimistic_course_percentage(my_grades, weights)
optimistic_letter_grade = GradeCalculator.calculate_letter_grade(optimistic_percentage_grade)
print(f'If all other assignments are 100%, the overall course would be {optimistic_percentage_grade*100}%, which is a {optimistic_letter_grade}')

# Compare standard weighting vs. project-heavy weighting side by side
standard_weights = GradeWeights()
heavy_weights = ProjectHeavyWeights()

standard_pct = GradeCalculator.calculate_course_percentage(my_grades, standard_weights)
heavy_pct = GradeCalculator.calculate_course_percentage(my_grades, heavy_weights)

standard_letter = GradeCalculator.calculate_letter_grade(standard_pct)
heavy_letter = GradeCalculator.calculate_letter_grade(heavy_pct)

print(f'Standard weights:      {standard_pct*100:.2f}% ({standard_letter})')
print(f'Project-heavy weights: {heavy_pct*100:.2f}% ({heavy_letter})')

# Testing letter grade boundary cutoffs
for v in [0.97, 0.93, 0.90, 0.87, 0.83, 0.80, 0.77, 0.73, 0.70, 0.60]:
    print(v, '->', GradeCalculator.calculate_letter_grade(v))
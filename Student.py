from grade import Grade

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []  # list of Grade objects

    def add_grade(self, grade):
        if not isinstance(grade, Grade):
            raise TypeError("Only Grade objects allowed")
        self.grades.append(grade)

    def calculate_gpa(self):
        if len(self.grades) == 0:
            return 0.0

        total_points = 0
        total_credits = 0

        for g in self.grades:
            total_points += g.get_grade_points() * g.course.credits
            total_credits += g.course.credits

        return round(total_points / total_credits, 2)

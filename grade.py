class Grade:
    VALID = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }

    def __init__(self, course, letter):
        if letter not in Grade.VALID:
            raise ValueError("Invalid grade")
        self.course = course
        self.letter = letter

    def get_grade_points(self):
        return Grade.VALID[self.letter]

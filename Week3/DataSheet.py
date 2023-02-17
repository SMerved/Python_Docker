class DataSheet():
    def __init__(self, courses):
        self.courses = courses
    def get_grades_as_list(self):
        grade_list = [c.grade for c in self.courses]
        return grade_list
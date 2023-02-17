class Student():
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        grade = 0
        grades = self.data_sheet.get_grades_as_list()
        for g in grades:
            grade += g
        grade_avg = grade/len(grades)
        return grade_avg
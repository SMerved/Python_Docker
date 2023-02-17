from Course import Course
from DataSheet import DataSheet
from Student import Student
import random, csv
from pathlib import Path

names = ["Jens", "Bob", "Hans", "Henrik", "Birgit", "Henriette", "Ingrid", "Merette"]
genders = ["Male", "Female"]
course1 = Course("Python", "2.03", "Thomas", 30, 7)
course2 = Course("Fullstack", "2.03", "Thomas/Jorg", 30, 2)
course3 = Course("Security", "2.03", "Daniel", 30, 0)
course4 = Course("GameDev", "2.03", "Jesper", 10, 10)
course5 = Course("Robotics", "2.03", "Tobias", 40, 4)
courses = [course1, course2, course3, course4, course5]
images = ["image1", "image2", "image3", "image4"]

def generate_students(names, genders, courses, images, n):
    for s in range(0,n):
        name = names[random.randint(0,len(names)-1)]
        gender = genders[random.randint(0,len(genders)-1)]
        data_set = set()
        for c in range(0, len(courses)):
            data_set.add(courses[random.randint(0, len(courses)-1)])
        course_list = list(data_set)
        data_sheet = DataSheet(course_list)
        image = images[random.randint(0, len(images)-1)]
        student = Student(name, gender, data_sheet, image)
        with open('students.csv', 'a', newline='') as students_file:
            output_writer = csv.writer(students_file)

            for sc in student.data_sheet.courses:
                output_writer.writerow([student.name, sc.name, sc.teacher, student.gender, sc.ects, sc.classroom, sc.grade, student.image_url])

def read_students(file):
    student_list = []
    data_sheet = []
    first = True
    with open(file, 'r'):
        csv_reader = csv.reader(file)
        csv_list = list(csv_reader)
        for row in csv_list:
            if(s_name!=row[0]):
                if(first != True):
                    student_list.append(Student(s_name, s_gender, data_sheet, s_image)) 
                s_name = row[0]
                s_gender = row[3]
                s_image = row[7]
                data_sheet = []
                first = False
            print(row)
            data_sheet.append(Course(row[1], row[5], row[2], row[4], row[6]))
    return student_list


            



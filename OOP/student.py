class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_student):
        self.name = name
        self.max_students = max_student
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
        else:
            print("It's over than the capacity of the class!")

    def get_average_grade(self):
        average = 0

        for student in self.students:
            average += student.grade

        return average / len(self.students)


student1 = Student("Danial", 21, 95)
student2 = Student("Behzad", 20, 85)
student3 = Student("Ali", 21, 75)

course1 = Course("Science", 3)
course2 = Course("Math", 2)

course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)

course2.add_student(student1)
course2.add_student(student2)
course2.add_student(student3)

print(course1.get_average_grade())
print(course2.get_average_grade())

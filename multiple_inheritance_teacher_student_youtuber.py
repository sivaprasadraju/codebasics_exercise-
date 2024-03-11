class Teacher:
    def teacher_role(self):
        print("Teacher")

class Engineer:
    def engineer_role(self):
        print("Engineer")

class Youtuber:
    def youtuber_role(self):
        print("Youtuber")

class Student(Teacher, Engineer, Youtuber):
    pass

person = Student()
person.teacher_role()
person.engineer_role()
person.youtuber_role()



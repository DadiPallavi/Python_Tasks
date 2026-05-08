class School:
    school_name="DR KKR GOWTHAM CONCEPUTAL SCHOOL"
    def __init__(self):
        pass
    def show_school(self):
        print("SCHOOL_NAME:",self.school_name)


class Teacher(School):
    teacher_name="varsha"
    subject="python"
    def __init__(self):
        pass
    def show_teacher(self):
        print("Teacher name:--", self.teacher_name)
        print("Subject:", self.subject)
        super().show_school()


class Student(Teacher):
    student_name="Pallavi"
    grade="A"
    def __init__(self):
        pass
    def show_student(self):
        print("Student Name:--", self.student_name)
        print("Grade:", self.grade)
        super().show_teacher()


p=Student()
p.show_student() 


    
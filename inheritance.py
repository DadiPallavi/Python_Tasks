#single inheritance
class course:
    course_name="Data Siecence"
    price=35000
    def show_course(self):
        print("data science course")
class programmingCourse(course):
    language="English"
    duration="6Months"
    def show_programming_course(self):
        print("child class data analycits ")
        print(self.language,self.duration)
        print(super().course_name,super().price)
        super().show_course()
o=programmingCourse()
o.show_programming_course()
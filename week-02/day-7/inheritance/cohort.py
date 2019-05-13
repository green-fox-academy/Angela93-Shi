from student import Student
from mentor import Mentor

class Cohort():
    def __init__(self,name):
        self.name = name
        self.students = []
        self.mentors = []
    
    def add_student(self,Student):
        self.students.append(Student)
        return self.students
    
    def add_mentor(self,Mentor):
        self.mentors.append(Mentor)
        return self.mentors
    
    def info(self):
        print(f"The {self.name} cohort has {len(self.students)} students and {len(self.mentors)} mentors.")

cohort = Cohort('Jane Doe')    
print(cohort.add_student(Student))
print(cohort.add_mentor(Mentor))
print(cohort.info())
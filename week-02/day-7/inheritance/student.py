from person import Person

class Student(Person):
    def __init__(self,Person,previous_organization,skipped_days):
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days
    
    def get_goal(self):
        print("Be a junior software develop")
    
    def introduce(self,person):
        print(f"Hi,I'm{person.name}, a {person.age} year old {person.gender} from {self.previous_organization} who skipped {self.skipped_days} from the course already. ")
    
    def skip_days(self,number_of_days):
        print(f"increase {self.skipped_days} by {number_of_days}")

person = Person('Jane Doe',30,'female')
student = Student(Person,'The School of Life',0)

print(student.get_goal())
print(student.introduce(person))
print(student.skip_days(2))
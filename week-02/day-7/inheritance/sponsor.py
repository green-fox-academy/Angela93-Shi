from person import Person

class Sponsor(Person):
    def __init__(self,name='Jane Doe',age=30,gender='female',company='Google',hired_students=0):
        Person.__init__(self,name='Jane Doe',age=30,gender='female')
        self.company = company
        self.hired_students = hired_students
    
    def introduce(self):
        print(f"Hi,I'm {self.name},a {self.age} year old {self.gender} who represents {self.company} and {self.hired_students} students so far")
    
    def hire(self):
        self.hired_students += 1
        return self.hired_students
    
    def get_goal(self):
        print("Hire brilliant junior software developers.")

# person = Person('Jane Doe',30,'female')
# sponsor = Sponsor(Person,'Googlr',0)

# print(sponsor.introduce(person))
# print(sponsor.hire())
# print(sponsor.get_goal())



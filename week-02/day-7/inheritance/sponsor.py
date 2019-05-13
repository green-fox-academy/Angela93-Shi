from person import Person

class Sponsor(Person):
    def __init__(self,Person,company,hired_students):
        self.company = company
        self.hired_students = hired_students
    
    def introduce(self,person):
        print(f"Hi,I'm {person.name},a {person.age} year old {person.gender} who represents {self.company} and {self.hired_students} students so far")
    
    def hire(self):
        self.hired_students += 1
        return self.hired_students
    
    def get_goal(self):
        print("Hire brilliant junior software developers.")

person = Person('Jane Doe',30,'female')
sponsor = Sponsor(Person,'Googlr',0)

print(sponsor.introduce(person))
print(sponsor.hire())
print(sponsor.get_goal())



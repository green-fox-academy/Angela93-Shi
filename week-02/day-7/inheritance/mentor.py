from person import Person

class Mentor(Person):
    def __init__(self,Person,level):
        self.level = level
    
    def get_goal(self):
        print("Educate brilliant junior software developers.")
    
    def introduce(self,person):
        print(f"Hi,I'm {person.name},a {person.age} year old {person.gender} {self.level} mentor.")

person = Person ('John Doe',30,'female')
mentor = Mentor(Person,'junior')

print(mentor.get_goal())
print(mentor.introduce(person))

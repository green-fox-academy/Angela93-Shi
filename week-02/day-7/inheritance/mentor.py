from person import Person

class Mentor(Person):
    def __init__(self,name='Jane Doe',age=30,gender='female',level='junior'):
        
        Person.__init__(self,name='Jane Doe',age=30,gender='female')
        self.level = level
    
    def get_goal(self):
        print("Educate brilliant junior software developers.")
    
    def introduce(self):
        print(f"Hi,I'm {self.name},a {self.age} year old {self.gender} {self.level} mentor.")

# person = Person ('John Doe',30,'female')
# mentor = Mentor(Person,'junior')

# print(mentor.get_goal())
# print(mentor.introduce(person))

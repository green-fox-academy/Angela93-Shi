# The Patient class doesn't depend on any other classes. It has two methods:
    # One to retrieve the severity of the disease.
    # One to treat the patient, it must decrease the severity by 1.
# The severity is a random number between 1 and 10, you can set it in the constructor or at the field declaration. Keep in mind, the severity cannot go below 0
import random
class Patient():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender =gender
        
    def severity(self):
        self.severity_level = random.randint(1,10)
        return self.severity_level

    def treat(self):
        try:
            if severity > 0:
                self.severity_level -= 1
        except:
            pass


# patient = Patient()
# patient.severity()
# patient.treat()
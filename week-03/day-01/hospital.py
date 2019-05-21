# It has a Queue which is set through the constructor.
# It has a method to add a Patient to the queue.
# It has a method to treat the next patient in the queue.


from patient import Patient
from my_queue import My_Queue

class Hospital:

    def __init__(self,my_queue):
        self.my_queue = my_queue

    def add_a_patient(self,patient):
        self.my_queue.addPatients(patient)

    def treat_next_patient(self):
        next_person = self.my_queue.get_next_person()
        for patient in self.my_queue:
            if patient == next_person:
                patient.treat()


my_queue = My_Queue()
patient1 = Patient('Lucy',38,'female')
patient2 = Patient('Nicy',56,'female')
my_queue.addPatients(patient1)
hospital = Hospital(my_queue)

hospital.add_a_patient(patient2)
hospital.treat_next_patient()

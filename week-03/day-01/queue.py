# If you have Patients you can create an abstract Queue class. It will hold the patients waiting for treatment.
    # It should have a method to add Patients to the queue.
    # It should have an abstract method to get the next patient.
# The implementation is up to you, you can store the patients in any data structure.

from patient import Patient

class Queue():
    def __init__(self,patients=[]):
        self.patients = patients
    
    def addPatients(self,patient):
        self.patients.append(patient)
        # print(self.patient_list)

    def get_next_person(self):
        pass

patient = Patient('Tony',56,'male')
queue = Queue()
queue.addPatients(patient)
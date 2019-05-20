# It should return always the next patient. (You need to track who was the last treated patient.)
# It should handle the cycles, so after the last patient it must return the first one again.
# Patients with 0 severity won't be returned ever. (You can remove them from the queue or just simple skip them)
# You can return null if all the patients have 0 severity or the queue is empty
from queue import Queue
from patient import Patient
class Class_Queue(Queue):
    def __init__(self,patients=[]):
        Queue.__init__(self,patients)
    
    def the_next_patient(self):
        while len(self.patients) != 0:
            for i in self.patients:
                if i.severity == 0:
                    self.patients.remove(i)
                else:
                    i.treat()
                    return f'{i.name}'

queue = Queue()
patient1 = Patient('Lucy',38,'female')
queue.addPatients(patient1)

class_queue = Class_Queue()
class_queue.the_next_patient()
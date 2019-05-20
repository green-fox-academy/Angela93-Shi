# It always returns the patient with the highest severity.
# If there are more patients with the same severity you can pick one, it is up to you which one is returned.
# Patients with 0 severity can be skipped or removed from the queue.
# You can return null if all the patients have 0 severity or the queue is empty
from patient import Patient
from queue import Queue

class Safe_Queue(Queue):
    def __init__(self,patients=[]):
        Queue.__init__(self,patients)

    def get_highest_severity(self):
        patient_dic={}
        for i in self.patients:
            if i.severity == 0:
                self.patients.remove(i)
            else:
                patient_dic[i.name] = i.severity
        
        if len(patient_dic) == 0:
            return None
        else:
            highest_patient = max(patient_dic.values())
            # print(highest_patient)
        for key in patient_dic:
            if patient_dic[key] == highest_patient:
                return key
    

# safe_queue = Safe_Queue()
# safe_queue.get_highest_severity()
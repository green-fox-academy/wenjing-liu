from patient import Patient

class Queue:
  def __init__(self):
    self.patient_list = []
  def add_patient(self, patient):
    if isinstance(patient, Patient):
      self.patient_list.append(patient)
  
  def get_next_patient(self, next):
    if len(self.patient_list):
      return self.patient_list[next].treat()
    else:
      return 'The queues is empty'
  def __str__(self):
    result = ''
    for patient in self.patient_list:
      result += patient.__str__() + ' '
    return result

'''
#### Queue class

If you have *Patient*s you can create an abstract *Queue* class. It will hold
the patients waiting for treatment.

- It should have a method to add *Patient*s to the queue.
- It should have an abstract method to get the next patient.

The implementation is up to you, you can store the patients in any data structure.
'''
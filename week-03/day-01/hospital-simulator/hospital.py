from queue import Queue
class Hospital:
  def __init__(self, queue):
    self.patient_queue = queue
  def add_patient(self, patient):
    self.patient_queue.add_patient(patient)
  def treat_next_patient(self):
    self.patient_queue.get_next_patient()

'''
#### Hospital class

Since you have *Queue* class and *Patient*s you can implement your *Hospital*
class as well. Which must fulfill the following requirements:

- It has a *Queue* which is set through the constructor.
- It has a method to add a *Patient* to the queue.
- It has a method to treat the next patient in the queue.
'''
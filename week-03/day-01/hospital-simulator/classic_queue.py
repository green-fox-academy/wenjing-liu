from queue import Queue

class ClassicQueue(Queue):
  def __init__(self):
    super(ClassicQueue, self).__init__()
    self.last_treadted_index = -1
  def get_next_patient(self):
    if len(self.patient_list):
      patient = None
      for index in range(self.last_treadted_index+1, len(self.patient_list)):
        if self.patient_list[index].severity > 1:
          patient = self.patient_list[index]
          self.last_treadted_index = index
          break
      if not patient:
        for index in range(0, self.last_treadted_index):
          if self.patient_list[index].severity > 1:
            patient = self.patient_list[index]
            self.last_treadted_index = index
            break
      if patient:
        patient.treat()
      else:
        return None 
    else:
      return None

  def __str__(self):
    return Queue.__str__(self)

'''
#### ClassicQueue class

The classic queue is a special queue which is not abstract anymore. Its method
to retrieve the next patient has the following specification

- It should return always the next patient. (You need to track who was the
  last treated patient.)
- It should handle the cycles, so after the last patient it must return the
  first one again.
- Patients with 0 severity won't be returned ever. (You can remove them from the
  queue or just simple skip them)
- You can return `null` if all the patients have 0 severity or the queue is empty
'''
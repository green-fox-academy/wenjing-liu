from queue import Queue

class SafeQueue(Queue):
  def __init__(self):
    super(SafeQueue, self).__init__()
  def get_next_patient(self):
    filtered_queue = list(filter(lambda patient: patient.severity > 0, self.patient_list))
    if len(filtered_queue) :
      patient = sorted(filtered_queue, key = lambda patient: patient.severity, reverse = True)[0]
      patient.treat()
    else:
      return None
  def __str__(self):
    return Queue.__str__(self)
  
'''
#### SafeQueue class

The safe queue is a special queue which is not abstract anymore. Its method
to retrieve the next patient has the following specification

- It always returns the patient with the highest severity.
- If there are more patients with the same severity you can pick one, it is up to
  you which one is returned.
- Patients with 0 severity can be skipped or removed from the queue.
- You can return `null` if all the patients have 0 severity or the queue is empty
'''
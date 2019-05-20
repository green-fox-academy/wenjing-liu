from patient import Patient
from hospital import Hospital
from safe_queue import SafeQueue
from classic_queue import ClassicQueue


def test_safe_queue():
  safe_queue = SafeQueue()
  hospital = Hospital(safe_queue)
  patient_1 = Patient('Claire')
  patient_2 = Patient('Duppy')
  patient_3 = Patient('Bob')
  hospital.patient_queue.add_patient(patient_1)
  hospital.patient_queue.add_patient(patient_2)
  hospital.patient_queue.add_patient(patient_3)
  print('Before', hospital.patient_queue)
  hospital.treat_next_patient()
  print('After', hospital.patient_queue)


def test_classic_queue():
  classic_queue = ClassicQueue()
  hospital = Hospital(classic_queue)
  patient_1 = Patient('Claire')
  patient_2 = Patient('Duppy')
  patient_3 = Patient('Bob')
  hospital.patient_queue.add_patient(patient_1)
  hospital.patient_queue.add_patient(patient_2)
  hospital.patient_queue.add_patient(patient_3)
  print('Before', hospital.patient_queue)
  hospital.treat_next_patient()
  print('After', hospital.patient_queue)


test_safe_queue()
test_classic_queue()
  

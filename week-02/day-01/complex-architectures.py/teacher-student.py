class Student:
  def __init__(self, name):
    self.name = name
  def learn(self):
    print(f'I am student {self.name}, I am learning.')
  def question(self, question, teacher):
    print(f'I am stundent {self.name}, I am asking {question}')
    teacher.answer(question)

class Teacher:
  def __init__(self, name):
    self.name = name
  def teach(self, student):
    print(f'I am teacher {self.name}, I am teaching.')
    student.learn()
  def answer(self, question):
    print(f'I am teacher {self.name}, I am answering {question}')

teacher = Teacher('Scott')
student = Student('Claire')
teacher.teach(student)
student.question('What is python?', teacher)
"""
# Teacher Student

 -  Create `Student` and `Teacher` classes
 -  `Student`
     -  `learn()`
     -  `question(teacher)` -> calls the teachers answer method
 -  `Teacher`
     -  `teach(student)` -> calls the students learn method
     -  `answer()`
"""
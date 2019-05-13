from person import Person

class Sponsor(Person):
  def __init__(self, name = 'Jane Doe', age = 30, gender = 'female', company = 'Google'):
    super().__init__(name, age, gender)
    self.company = company
    self.hired_students = 0
  
  def introduce(self):
    print(f'Hi, I\'m {self.name}, a {self.age} year old {self.gender} who represents {self.company} and hired {self.hired_students} students so far.')
  
  def hire(self):
    self.hired_students += 1
  
  def get_goal(self):
    print('Hire brilliant junior software developers.')

sponsor = Sponsor('Jane Doe', 30, 'female', 'Google')
sponsor.introduce()
sponsor.get_goal()
sponsor.hire()
sponsor.introduce()


"""
Create a Sponsor class that has the same fields and methods as the Person class, and has the following additional

fields:
company: name of the company
hired_students: number of students hired
method:
introduce(): "Hi, I'm name, a age year old gender who represents company and hired hired_students students so far."
hire(): increase hired_students by 1
get_goal(): prints out "Hire brilliant junior software developers."
The Sponsor class has the following constructors:

Sponsor(name, age, gender, company): beside the given parameters, it sets hired_students to 0
Sponsor(): sets name to Jane Doe, age to 30, gender to female, company to Google and hired_students to 0
"""
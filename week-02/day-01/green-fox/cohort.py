from student import Student
from mentor import Mentor

class Cohort:
  def __init__(self, name):
    self.name = name
    self.students = []
    self.mentors = []
  
  def add_student(self, student):
    if isinstance(student, Student):
      self.students.append(student)
  
  def add_mentor(self, mentor):
    if isinstance(mentor, Mentor):
      self.mentors.append(mentor)

  def info(self):
    print(f'The {self.name} cohort has {len(self.students)} students and {len(self.mentors)} mentors.')

"""
Create a Cohort class that has the following

fields:
name: the name of the cohort
students: a list of Students
mentors: a list of Mentors
methods:
add_student(Student): adds the given Student to students list
add_mentor(Mentor): adds the given Mentor to mentors list
info(): prints out "The name cohort has len(students) students and len(mentors) mentors."
The Cohort class has the following constructors:

Cohort(name): beside the given parameter, it sets students and mentors as empty lists
"""
from person import Person

class Mentor(Person):
  def __init__(self, name = 'Jane Doe', age = 30, gender = 'female', level = 'intermediate'):
    Person.__init__(self, name, age, gender)
    self.level = level
  
  def get_goal(self):
    print('Educate brilliant junior software developers.')

  def introduce(self):
    print(f'Hi, I\'m {self.name}, a {self.age} year old {self.gender} {self.level} mentor.')

mentor = Mentor('Jane Doe', 30, 'female', 'intermediate')
mentor.introduce()
mentor.get_goal()

"""
Create a Mentor class that has the same fields and methods as the Person class, and has the following additional

fields:
level: the level of the mentor (junior / intermediate / senior)
methods:
get_goal(): prints out "Educate brilliant junior software developers."
introduce(): "Hi, I'm name, a age year old gender level mentor."
The Mentor class has the following constructors:

Mentor(name, age, gender, level)
Mentor(): sets name to Jane Doe, age to 30, gender to female, level to intermediate
"""
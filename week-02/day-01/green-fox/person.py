class Person:
  def __init__(self, name = 'Jane Doe', age = 30, gender = 'female'):
    self.name = name
    self.age = int(age)
    self.gender = gender
  def introduce(self):
    print(f'Hi, I\'m {self.name}, {self.age} year old {self.gender}.')
  def get_goal(self):
    print('My goal is: Live for the moment!')


person_1 = Person('Jane Doe', 30, 'female')
person_1.introduce()
person_1.get_goal()
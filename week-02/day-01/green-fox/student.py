from person import Person

class Student(Person):
  def __init__(self, name = 'Jane Doe', age = 30, gender = 'female', previous_organization = 'The School of Life', skipped_days = 0):
    super().__init__(name, age, gender)
    self.previous_organization = previous_organization
    self.skipped_days = skipped_days
  
  def get_goal(self):
    print('Be a junior software developer.')
  
  def introduce(self):
    print(f'Hi, I\'m {self.name}, {self.age} year old {self.gender} from {self.previous_organization} who skipped {self.skipped_days} days from the course already.')
  def skip_days(self, number_of_days):
    self.skipped_days += number_of_days


stundent = Student('Jane Doe', 30, 'female', 'The School of Life', 0)
# stundent.introduce()
stundent.get_goal()
stundent.skip_days(3)
# stundent.introduce()

from kid import Kid
from santa import Santa
from school import School

def test():
  kid_1 = Kid('Claire', 10)
  kid_2 = Kid('Bob', 13, False)
  kid_3 = Kid('Lucy', 12)
  santa = Santa('Santa', 60)
  school = School()
  school.enroll_a_kid(kid_1)
  school.enroll_a_kid(kid_2)
  school.enroll_a_kid(kid_3)
  print('school: ', school.kid_status())
  print('santa: ', santa.introduce())
  print('Celebrate Chirs')
  school.celebrage_christmas(santa)
  print('school: ', school.kid_status())
  print('santa: ', santa.introduce())

test()
import collections

Student = collections.namedtuple('Student', 'name age gender grades')

student_1 = Student(name='John', age=16, gender='male', grades=[5, 5, 4, 2])
student_2 = Student(name='Jane', age=15, gender='female', grades=[4, 3, 4, 4, 5])
student_3 = Student(name='Bob', age=17, gender='male', grades=[2, 2, 3, 1])
student_4 = Student(name='Claire', age=18, gender='female', grades=[5, 5, 4, 4])

students = [student_1, student_2, student_3, student_4]

print('list that only includes the boys: \n',list(filter(lambda stu: stu.gender == 'male', students)))

print('list that only includes who\'s name starts with the letter J:\n', 
  list(filter(lambda stu: stu.name.startswith('J'), students)))

print('list that only includes the girls:\n', 
  list(filter(lambda stu: stu.gender == 'female', students)))

print('list that only includes the boys who\'s name starts with the letter J:\n', 
  list(filter(lambda stu: stu.gender=='male' and stu.name.startswith('J'), students)))


print('list that only includes the boys who\'s name starts with the letter J:\n', 
  list(filter(lambda stu: stu.gender=='male' and stu.name.startswith('J'), students)))

print('list that only includes the girls who\'s grade average is above 4: \n', 
  list(filter(lambda stu: sum(stu.grades)/len(stu.grades) > 4 and stu.gender=='female', students)))

print('list have two 5s', list(filter(lambda stu: len(list(filter(lambda n: n==5, stu.grades))) == 2, students)))

print('list avg above 4 and  two 5s\n', list(filter(lambda stu: len(list(filter(lambda n: n==5, stu.grades))) == 2 and sum(stu.grades)/len(stu.grades) > 4, students)))

"""
# Students

Given a list of students with the following fields: `name`, `age`, `gender` and
`grades`.

- Create a new list that only includes the boys
- Create a new list that only includes who's name starts with the letter J
- Create a new list that only includes the girls
- Create a new list that only includes who's grade average is above 4
- Create a new list that only includes the boys who's name starts with the
  letter J
- Create a new list that only includes the girls who's grade average is above 4
- Create a new list that only includes who's at least two 5s
- Create a new list that only includes who's grade average is above 4 and at
  at least got two 5s

Some example data

| name | age | gender | grades        |
|:-----|:----|:-------|:--------------|
| John | 16  | male   | 5, 5, 4, 2    |
| Jane | 15  | female | 4, 3, 4, 4, 5 |
| Bob  | 17  | male   | 2, 2, 3, 1    |
"""
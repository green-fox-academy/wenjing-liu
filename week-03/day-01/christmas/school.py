from kid import Kid
from santa import Santa

class School:
  def __init__(self):
    self.kid_list = []
  def enroll_a_kid(self, kid):
    if isinstance(kid, Kid):
      self.kid_list.append(kid)
  def celebrage_christmas(self, santa):
    if isinstance(santa, Santa):
      santa.assign_gifts(self.kid_list)
  def kid_status(self):
    result = ''
    for kid in self.kid_list:
      result += kid.introduce() + '\n'
    return result

'''
#### School

```
Properties
- list of kids

Behaviour
- enroll a new `Kid`
  - it should get a Kid as a parameter
  - add the new Kid to the `list of kids`
  - 

- have Christmas
  - it should get a Santa as a parameter
  - call Santa's `assign gifts` behaviour
```
'''
import re

pattern = re.compile('(\w+\.?\w+?)@greenfox\.?academy(?:\.com)?')

emails = ['john@greenfoxacademy.com', 'jane.doe@greenfoxacademy.com', 'jane@greenfox.academy', '', 'john@wick.com', 'jane@citromail.hu', 'janegreenfoxacademy.co']

for email in emails:
  result = pattern.match(email)
  if result:
    print(f'{email} capture is:', result.groups())
  else:
    print('Not matched')
tel_book = {
  'William A. Lathan': 405-709-1865,
  'John K. Miller': 402-247-8568,
  'Hortensia E. Foster': 606-481-6467,
  'Amanda D. Newland': 319-243-5613,
  'Brooke P. Askew': 307-687-2982
}

def tel_search(book):
  print(f'What is John K. Miller\'s phone number?')
  if 'John K. Miller' in book:
    print(f"Answer: {tel_book['John K. Miller']}")
  else:
    print('Sorry, we do not have John K. Miller\'s number')
  
  print('Whose phone number is 307-687-2982?')
  record_key = None
  for key, value in book.items():
    if value == '307-687-298':
      record_key = key 
      break
  if record_key:
    print(f'Answer: {record_key}')
  else:
    print('Sorry, we do not have this number in the book')
  
  print('Do we know Chris E. Myers\' phone number?')
  if 'Chris E. Myer' in book:
    print(f"Answer: yes, his number is {tel_book['Chris E. Myer']}")
  else:
    print('Sorry, we do not know Chris E. Myers\' number')
  

tel_search(tel_book)


"""
# Telephone book

We are going to represent our contacts in a map where the keys are going to be
strings and the values are going to be strings as well.

- Create a map with the following key-value pairs.

| Name (key)          | Phone number (value) |
|:--------------------|:---------------------|
| William A. Lathan   | 405-709-1865         |
| John K. Miller      | 402-247-8568         |
| Hortensia E. Foster | 606-481-6467         |
| Amanda D. Newland   | 319-243-5613         |
| Brooke P. Askew     | 307-687-2982         |

- Create an application which solves the following problems.
  - What is John K. Miller's phone number?
  - Whose phone number is 307-687-2982?
  - Do we know Chris E. Myers' phone number?
"""
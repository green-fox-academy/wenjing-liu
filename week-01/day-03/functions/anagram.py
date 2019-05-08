def is_anagram(str1, str2):
  str1_copy = str1.lower().replace(' ', '')
  str2_copy = str2.lower().replace(' ', '')

  str1_set = set(str1_copy)
  str2_set = set(str2_copy)
  is_anagram = False 
  if str1_set == str2_set:
    is_anagram = True
    for value in str1_set:
      if str1_copy.count(value) != str2_copy.count(value):
        is_anagram = False
        break
  return is_anagram


print(is_anagram('Dog', 'GoD'))
print(is_anagram('green', 'fox'))

print(is_anagram('customers', 'store scum'))


"""
## Anagram

### What the hell is an anagram?
> An anagram is direct word switch or word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; for example, the word anagram can be rearranged into nag-a-ram.
> *[for more detail check [anagram](https://en.wikipedia.org/wiki/Anagram) on Wikipedia]*

### Exercise
Create a function named **is anagram** following your current language's style guide. It should take two strings and return a boolean value depending on whether its an anagram or not.

### Examples
|input 1|input 2|output|
|:-----:|:-----:|:---:|
|"dog"|"god"|true|
|"green"|"fox"|false|
"""
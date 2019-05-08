
def create_palindrome(string):
  return string + string[::-1]

print(create_palindrome('123'))
print(create_palindrome('greenfox'))
print(create_palindrome('dfg cdf'))

"""
## Palindrome builder

### What the hell is a palindrome?

> A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar.
> *[for more detail check [palindrome](https://en.wikipedia.org/wiki/Palindrome) on Wikipedia]*

### Exercise

Create a function named **create palindrome** following your current language's style guide. It should take a string, create a palindrome from it and then return it.

### Examples

|input|output|
|:---:|:---:|
|""|""|
|"greenfox"|"greenfoxxofneerg"|
|"123"|"123321"|
"""
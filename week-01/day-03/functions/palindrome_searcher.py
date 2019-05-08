
def get_all_pali(string):
  length = len(string)
  gap = '_'
  pd = {}
  pd_str = []

  for i in range(length):
    pd[str(i) + gap + str(i)] = True

  for sub_len in range(2, length+1):
    for i in range(0, length+1 - sub_len):
      j = i + sub_len - 1
      if sub_len == 2:
        pd[str(i) + gap + str(j)] = string[i] == string[j]
      else:
        pd[str(i) + gap + str(j)] = string[i] == string[j] and pd[str(i+1) + gap + str(j-1)]

  for key, value in pd.items():
    if value:
      indexes = list(key.split('_'))
      start = int(indexes[0])
      end = int(indexes[1]) + 1
      pd_str.append(string[start:end])
      
  return pd_str

def get_pali(string, length = 3):
  all_pd = get_all_pali(string)
  pali = []
  for sub_pali in all_pd:
    if len(sub_pali) >= length:
      pali.append(sub_pali)
  return pali


# get_all_pali('racecar')
print(get_pali('racecar'))





"""
## Palindrome searcher

[What the hell is a palindrome?](palindrome-builder/palindrome-builder.md)

### Exercise

Create a function named **search palindrome** following your current language's style guide. It should take a string, search for palindromes that at least 3 characters long and return a list with the found palindromes.

### Examples

|input|output|
|:---:|:---:|
|"dog goat dad duck doodle never"|["og go", "g g", " dad ", "dad", "d d", "dood", "eve"]|
|"apple"|[]|
|"racecar"|["racecar", "aceca", "cec"]|
|""|[]|

"""
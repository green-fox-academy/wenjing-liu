
#  Create a function that takes two strings as a parameter
#  Returns the starting index where the second one is starting in the first one
#  Returns `-1` if the second string is not in the first one

def substr(str, keyword):
    index = str.find(keyword)
    if index > -1:
      return index
    return -1

#  Example
# should print: `17`
print(substr("this is what I'm searching in", "searching"))

# should print: `-1`
print(substr("this is what I'm searching in", "not"))
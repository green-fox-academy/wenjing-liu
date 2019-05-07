# - Create an array variable named `numList`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Double all the values in the array
numList = [3, 4, 5, 6, 7]

for i in range(len(numList)):
  numList[i] *= 2
print(numList)
# Write a function that copies the contents of a file into another
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def copy_file(soure_file, dest_file):
  try:
    with open(soure_file, 'r') as source:
      with open(dest_file, 'a') as dest:
        dest.truncate(0)
        for line in source:
          dest.write(line)
    return True
  except Exception as e:
    print('Error occurs:', e)
    return False

print(copy_file('source.txt', 'dest.txt'))
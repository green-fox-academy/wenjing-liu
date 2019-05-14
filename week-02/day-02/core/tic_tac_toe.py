# Write a function that takes a filename as a parameter
# The file contains an ended Tic-Tac-Toe match
# We have provided you some example files (draw.txt, win-x.txt, win-o.txt)
# Return "X", "O" or "Draw" based on the input file

def tic_tac_result(filename):
  try:
    with open(filename, 'r') as file:
      return file.read()
  except Exception as e:
    print(f'Error occurs whe read {filename}: {e}')
    

print(tic_tac_result("win-o.txt"))
# Should print "O"

print(tic_tac_result("win-x.txt"))
# Should print "X"

print(tic_tac_result("draw.txt"))
# Should print "Draw"
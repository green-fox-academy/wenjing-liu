cost_list = [500, 1000, 1250, 175, 800, 120]

def finance_report(cost):
  print(f'How much did we spend? Answer: {sum(cost_list)}')
  print(f'Which was our greatest expense? Answer: {max(cost_list)}')
  print(f'Which was our cheapest spending? Answer: {min(cost_list)}')
  print(f'What was the average amount of our spendings? Answer: {sum(cost_list)/len(cost_list)}')

finance_report(cost_list)



"""
# Personal finance

We are going to represent our expenses in a list containing integers.

- Create a list with the following items.
  - 500, 1000, 1250, 175, 800 and 120
- Create an application which solves the following problems.
  - How much did we spend?
  - Which was our greatest expense?
  - Which was our cheapest spending?
  - What was the average amount of our spendings?
"""
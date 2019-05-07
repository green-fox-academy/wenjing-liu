current_hours = 14;
current_minutes = 34;
current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented by the variables
seconds_in_a_day = 24 * 60 * 60
past_seconds = current_hours * current_minutes * current_seconds
remaining_seconds = seconds_in_a_day - past_seconds

print(f'The remaings seconds of current day is {remaining_seconds}')
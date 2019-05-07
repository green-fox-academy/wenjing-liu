# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
#
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52

daily_coding_hour = 6
semester_last_weeks = 17
work_days_per_week = 5
coding_hours_total = daily_coding_hour * semester_last_weeks * work_days_per_week 
print(f'If the attendee only codes on workdays, he/she will coding {coding_hours_total} hours in the semester.')

average_working_hour_weekly = 52

perc_coding_hour = (coding_hours_total / (semester_last_weeks * average_working_hour_weekly)) * 100
print(f'The percentage of the coding hours in the semester is {perc_coding_hour}%')
"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

import sys
import calendar
from datetime import datetime

user_input = sys.argv
today = datetime.today()

# If no user input, print calendar for current month
if len(user_input) == 1:
    print(calendar.month(today.year, today.month))

# If one argument only, assume it's the month and print that month for this year
elif len(user_input) == 2:
    month = int(user_input[1])
    print(calendar.month(today.year, month))

elif len(user_input) == 3:
    month = int(user_input[1])
    year = int(user_input[2])
    print(calendar.month(year, month))

else:
    print('\nThe program expects month and year as integers, separated by spaces. Example: "5 2001". Try again.')
#!/usr/bin/python

# Here's how you test this:
# 1) ./fizz_buzz.py [Enter], then enter a number between 1 - 1000+
# 2) ./fizz_buzz.py [Enter], then enter your name
# 3) ./fizz_buzz.py Carlos
# 4) ./fizz_buzz.py 1
# 5) ./fizz_buzz.py 123
# 6) ./fizz_buzz.py [Enter] and then hit CTRL+C



# I'm importing sys and os for basic functions.  
# sys for passing arguments into the script, and os for display control
import sys
import os

# I'm checking to see if an argument is passed to the script
# If the argument is not provided, then we prompt for user input
# If an argument is provided, we assign x to that argument.
# If the user decides to cancel by hitting CTRL+C or other break command, we use try to give a friendly message and then exit the script.
try:
  if not len(sys.argv) > 1:
    print ""
    x = raw_input("     Give us a number larger than 1: ")
    print ""
  else:
    x = sys.argv[1]
except KeyboardInterrupt:
  os.system('clear')
  print ""
  print "     Fine, then we won't play after all.  Run on home..."
  print
  sys.exit(1)


# We take x and place it at the end of a range assigned to n.  
# However, I want to check to make sure the argument is an integer
# So I will use try to detect an argument other than an integer 
# and except the ValueError and print a friendly message and then exit
# I also want to include the number that the user inputs so I add 1 to the integer
# I feel like it will be less confusing as to why the user input isn't included in the print out
try:
  n = range (0,int(x)+1)
except ValueError:
  os.system('clear')
  print
  print "     You entered " + x + ".  We need some numbers >= 1.  Please try again."
  print
  sys.exit(1)

  
# assign message to a variable.  I will use this later to count number of characters.
message = 'Fizz Buzz counting up to '

# Let's clear the screen
# Print the initial message and underline it from the length of the message + argument
os.system('clear')
print message + x
print ('-' * len(str(message)))+('-' * len(str(x)))


# the ol' for loop.  Our range starts at 0, but normally humans will see a list begin with 1, so I want to ignore 0
# then we check for True / False statements based on looping thru the range of n.
# If nothing matches, simply print the number out in the range.
# And that's it...
for number in n:
  if number == 0:
    pass
  elif number % 3 == 0 and number % 5 == 0:
    print "Fizz Buzz"
  elif number % 3 == 0:
    print "Fizz"
  elif number % 5 == 0:
    print "Buzz"
  else:
    print number
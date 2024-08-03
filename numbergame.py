import random
import math
lower_range = int(input("Enter Lower range:- "))
upper_range = int(input("Enter Upper range:- "))
random_number = random.randint(lower_range, upper_range)
print("\n\tYou've only ", 
	round(math.log(upper_range - lower_range + 1, 2)),
	" chances to guess the integer!\n")
count = 0
while count < math.log(upper_range - lower_range + 1, 2):
	count += 1
	guess = int(input("Guess a number:- "))
	if random_number == guess:
		print("Congratulations you did it in ",
			count, " try")
		break
	elif random_number > guess:
		print("You guessed too small!")
	elif random_number < guess:
		print("You Guessed too high!")
if count >= math.log(upper_range - lower_range + 1, 2):
	print("\nThe number is %d" % random_number)
	print("\tBetter Luck Next time!")
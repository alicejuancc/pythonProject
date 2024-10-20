"""
File: coin_flip_runs.py
Name: Alice
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	In this program, user will enter a number, which is the time of runs. The program will stop once the random
	coin reaches the time.
	"""
	print("Let's flip a coin!")
	num_runs = int(input('Number of runs: '))
	result = ''  # record the flip result
	while True:
		if num_runs == 0:
			print('Number of runs is 0.')
			break
		else:
			num_flip = r.randrange(1, 3)
			if num_flip == 1:
				result += "H"
			else:
				result += "T"
			is_the_first_same = True
			same_count = 0
			for i in range(len(result)-1):
				if result[i] == result[i+1]:
					if is_the_first_same:
						same_count += 1
						is_the_first_same = False
				else:
					is_the_first_same = True
			if same_count == num_runs:
				print(result)
				break


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()

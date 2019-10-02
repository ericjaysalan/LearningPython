import random


def show_user_prompt():
	print('String Methods:')
	print(f'1.{upper_method}\t6.{islower_method}\t11.{isalpha_method}')
	print(f'2.{lower_method}\t7.{isupper_method}\t12.{isnumeric_method}')	
	print(f'3.{title_method}\t8.{replace_method}\t13.{isalnum_method}')
	print(f'4.{capitalize_method}\t9.{index_method}\t14.{len_function}')
	print(f'5.{find_method}\t10.{istitle_method}\t15.{split_method}')
	print()


user_string = user_argument = user_argument1 = user_argument2 = proceed = ''
# user_string = ''
# user_argument = ''
# user_argument1 = ''
# proceed = ''
counter = argument_count = 0

argument_count_prompt = '> How many arguments would you like to enter? '
enter_string_prompt = '> Enter String: '
again_prompt = '> Again? [Y] or [N] '
choose_another_method_prompt = '> Choose another method? [Y] or [N] '

invalid_command_message = '> !!! INVALID COMMAND. METHOD NOT FOUND. ENTER AGAIN. !!!'

upper_method, lower_method = 'upper()', 'lower()'
# upper_method = 'upper()'
# lower_method = 'lower()'
title_method = 'title()'
capitalize_method = 'capitalize()'
find_method = 'find()'
islower_method = 'islower()'
isupper_method = 'isupper()'
replace_method = 'replace()'
index_method = 'index()'
istitle_method = 'istitle()'
isalpha_method = 'isalpha()'
isnumeric_method = 'isnumeric()'
isalnum_method = 'isalnum()'
split_method = 'split()'
len_function = 'len()'

while True:
	show_user_prompt()

	string_method_to_be_used = input('> ')
	print()

	# If instead the user doesn't want to test anymore methods, but he's in the choices prompt, he can type exit.
	if string_method_to_be_used.lower() == 'exit' or string_method_to_be_used.lower() == 'quit':
		break

	# Converts the input to int for the method choices.
	string_method_to_be_used = int(string_method_to_be_used)

	# upper()
	if string_method_to_be_used == 1:
		while True:
			print(f'> The {upper_method} method converts all alphabetic characters to their uppercase characters. Symbols are ignored.')
			print()
			user_string = input(enter_string_prompt)
			print()

			print(' Processing ...')
			while counter < random.randint(10, 20):
				print(' ...')
				counter += 1

			print()
			print(f'> Your string: {user_string}')
			print(f'> {upper_method} method applied: ' + user_string.upper())
			print()

			proceed = input(again_prompt)
			print()
			if proceed.lower() == 'n':
				break

		print()
		proceed = input(choose_another_method_prompt)
		print()
		if proceed.lower() == 'n':
			break

	# lower()
	elif string_method_to_be_used == 2:
		while True:
			print(f'> The {lower_method} method converts all alphabetic characters to their lowercase characters. Symbols are ignored.')
			print()
			user_string = input(enter_string_prompt)
			print()

			print('> Processing ...')
			while counter < random.randint(10, 20):
				print(' ...')
				counter += 1

			print()
			print(f'> Your string: {user_string}')
			print(f'> {lower_method} applied: ' + user_string.lower())
			print()

			proceed = input(again_prompt)
			print()
			if proceed.lower() == 'n':
				break

		print()
		proceed = input(choose_another_method_prompt)
		print()
		if proceed.lower() == 'n':
			break

	# title()
	elif string_method_to_be_used == 3:
		while True:
			print(f'> The {title_method} method converts all first alphabetic characters separated by a space to their uppercase characters. Symbols are ignored.')
			print()
			user_string = input(enter_string_prompt)
			print()

			print('> Processing ...')
			while counter < random.randint(10, 20):
				print(' ...')
				counter += 1

			print()
			print(f'> Your string: {user_string}')
			print(f'> {title_method} applied: ' + user_string.title())
			print()

			proceed = input(again_prompt)
			print()
			if proceed.lower() == 'n':
				break

		print()
		proceed = input(choose_another_method_prompt)
		print()
		if proceed.lower() == 'n':
			break

	# capitalize()
	elif string_method_to_be_used == 4:
		while True:
			print(f'> The {capitalize_method} method converts the first alphabetic character of the string to it\'s respective uppercase character. All other alphabetic characters are changed to their lowercase characters. Symbols are ignored.')
			print()
			user_string = input(enter_string_prompt)
			print()

			print('> Processing ...')
			while counter < random.randint(10, 20):
				print(' ...')
				counter += 1

			print()
			print(f'> Your string: {user_string}')
			print(f'> {capitalize_method} applied: ' + user_string.capitalize())
			print()

			proceed = input(again_prompt)
			print()
			if proceed.lower() == 'n':
				break

		print()
		proceed = input(choose_another_method_prompt)
		print()
		if proceed.lower() == 'n':
			break

	# find()
	elif string_method_to_be_used == 5:
		while True:
			print(f'> The {find_method} method finds the index number of the substring, or a string part of another string, that is the argument given to this method. {find_method} method can optionally take a second argument which is where Python will start to search for the first argument. A third argument can also be optionally added to specify what index to end the search for the first argument. Remember that Python is case sensitive.')
			print()
			user_string = input(enter_string_prompt)
			print()
			argument_count = int(input(argument_count_prompt))
			print()

			# 1 argument
			if argument_count == 1:
				user_argument = input('> Enter argument: ')
				print()
				print('> Processing ...')
				while counter < random.randint(10, 20):
					print(' ...')
					counter += 1

				print()
				print(f'> Your string: {user_string}')
				print(f'> {find_method} applied with argument: ', user_string.find(user_argument))
				print()
				if user_string.find(user_argument) == -1:
					print('As you can see, the result is -1. It means the argument you gave is nowhere to be found in the string.')
					print()
				proceed = input(again_prompt)
				if proceed.lower() == 'n':
					break

			# 2 arguments
			elif argument_count == 2:
				user_argument = input('> Enter first argument: ')
				user_argument1 = int(input('> Enter second argument: '))
				print()
				print('> Processing ...')
				while counter < random.randint(10, 20):
					print(' ...')
					counter += 1

				print()
				print(f'> Your string: {user_string}')
				print(f'> {find_method} applied with 2 argument: ', user_string.find(user_argument, user_argument1))
				print()
				if user_string.find(user_argument, user_argument1) == -1:
					print('As you can see, the result is -1. It means the argument you gave is nowhere to be found in the string or within the starting index of the argument you gave.')
					print()
				proceed = input(again_prompt)
				if proceed.lower() == 'n':
					break

			# 3 arguments
			elif argument_count == 3:
				user_argument = input('> Enter first argument: ')
				user_argument1 = int(input('> Enter second argument: '))
				user_argument2 = int(input('> Enter third argument: '))

				print()
				print('> Processing ...')
				while counter < random.randint(10, 20):
					print(' ...')
					counter += 1

				print()
				print(f'> Your string: {user_string}')
				print(f'> {find_method} applied with 3 argument: ', user_string.find(user_argument, user_argument1, user_argument2))
				print()
				if user_string.find(user_argument, user_argument1, user_argument2) == -1:
					print('As you can see, the result is -1. It means the argument you gave is nowhere to be found in the string or within the two index numbers which were the arguments you gave.')
					print()
				proceed = input(again_prompt)
				print()
				if proceed.lower() == 'n':
					break

				else:
					print(invalid_command_message)

		print()
		proceed = input(choose_another_method_prompt)
		print()
		if proceed.lower() == 'n':
			break

	# islower()
	elif string_method_to_be_used == 6:
		while True:
			print(f'> The {islower_method} method returns a boolean value of True or False if the string is composed of ONLY lowercase alphabetic characters. Whitespace characters and symbols are ignored.')
			print()
			user_string = input(enter_string_prompt)
			print()

			print('> Processing ...')
			while counter < random.randint(10, 20):
				print(' ...')
				counter += 1

			print()
			print(f'> Your string: {user_string}')
			print(f'> {islower_method} applied:', user_string.islower())
			print()

			proceed = input(again_prompt)
			print()
			if proceed.lower() == 'n':
				break

		print()
		proceed = input(choose_another_method_prompt)
		print()
		if proceed.lower() == 'n':
			break

	# isupper()
	elif string_method_to_be_used == 7:
		while True:
			print(f'> The {isupper_method} method returns a boolean value of True or False if the string is composed of ONLY uppercase alphabetic characters. Whitespace characters and symbols are ignored.')
			print()
			user_string = input(enter_string_prompt)
			print()

			print('> Processing ...')
			while counter < random.randint(10, 20):
				print(' ...')
				counter += 1

			print()
			print(f'> Your string: {user_string}')
			print(f'> {isupper_method} applied:', user_string.isupper())
			print()

			proceed = input(again_prompt)
			if proceed.lower() == 'n':
				break

		print()
		proceed = input(choose_another_method_prompt)
		print()
		if proceed.lower() == 'n':
			break

	# replace()
	elif string_method_to_be_used == 8:
		while True:
			print(f'> The {replace_method} method takes two arguments. The first positional argument determines what the substring to find is, and the other one determines what to replace it with.')
			print()
			user_string = input(enter_string_prompt)
			user_argument = input('> Enter first argument: ')
			user_argument1 = input('> Enter second argument: ')
			print()

			print('> Processing ...')
			while counter < random.randint(10, 20):
				print(' ...')
				counter += 1

			print()
			print(f'> Your string: {user_string}')
			print(f'> {replace_method} applied with arugment: ' + user_string.replace(user_argument, user_argument1))
			print()

			proceed = input(again_prompt)
			print()
			if proceed.lower() == 'n':
				break

		print()
		proceed = input(choose_another_method_prompt)
		print()
		if proceed.lower() == 'n':
			break

	# index()
	elif string_method_to_be_used == 9:
		print(f'The {index_method} is currently unavailable.')
		# while True:
		# 	print(f'> The {index_method} method finds the index number of the substring, or a string part of another string, that is the argument given to this method. {index_method} method can optionally take a second argument which is where Python will start to search for the first argument. A third argument can also be optionally added to specify what index to end the search for the first argument. The difference between the {index_method} and {find_method} is that if the subtring is not found in the {index_method}, it returns an exception. Therefore, it\'s much safer to use the {find_method}. Remember that Python is case sensitive.')
		# 	print()
		# 	user_string = input(enter_string_prompt)
		# 	user_argument = input('> Enter argument: ')
		# 	print()

		# 	print('> Processing ...')
		# 	while counter < random.randint(5, 20):
		# 		print(' ...')
		# 		counter += 1

		# 	print()
		# 	print(f'> Your string: {user_string}')
		# 	print(f'> {index_method} applied with arugment: ' + user_string.index(user_argument))
		# 	print()

		# 	proceed = input(again_prompt)
		# 	if proceed.lower() == 'n':
		# 		break

	# istitle()
	elif string_method_to_be_used == 10:
		while True:
			print(f'> The {istitle_method} method returns a boolean value of True or False if the string\'s first alphabetic letters of words are ALL are in uppercase. Whitespace characters and symbols are ignored.')
			print()
			user_string = input(enter_string_prompt)
			print()

			print('> Processing ...')
			while counter < random.randint(10, 20):
				print(' ...')
				counter += 1

			print()
			print(f'> Your string: {user_string}')
			print(f'> {istitle_method} applied:', user_string.istitle())
			print()

			proceed = input(again_prompt)
			print()
			if proceed.lower() == 'n':
				break

		print()
		proceed = input(choose_another_method_prompt)
		print()
		if proceed.lower() == 'n':
			break

	# isalpha()
	elif string_method_to_be_used == 11:
		while True:
			print(f'> The {isalpha_method} method returns a boolean value of True or False if the string is of ONLY composed of alphabetic characters.')
			print()
			user_string = input(enter_string_prompt)
			print()

			print('> Processing ...')
			while counter < random.randint(10, 20):
				print(' ...')
				counter += 1

			print()
			print(f'> Your string: {user_string}')
			print(f'> {isalpha_method} applied:', user_string.isalpha())
			print()

			proceed = input(again_prompt)
			print()
			if proceed.lower() == 'n':
				break

		print()
		proceed = input(choose_another_method_prompt)
		print()
		if proceed.lower() == 'n':
			break

	# isnumeric()
	elif string_method_to_be_used == 12:
		while True:
			print(f'> The {isnumeric_method} method returns a boolean value of True or False if the string is composed ONLY of numeric characters.')
			print()
			user_string = input(enter_string_prompt)
			print()

			print('> Processing ...')
			while counter < random.randint(10, 20):
				print(' ...')
				counter += 1

			print()
			print(f'> Your string: {user_string}')
			print(f'> {isnumeric_method} applied:', user_string.isnumeric())
			print()

			proceed = input(again_prompt)
			print()
			if proceed.lower() == 'n':
				break

		print()
		proceed = input(choose_another_method_prompt)
		print()
		if proceed.lower() == 'n':
			break

	# isalnum()
	elif string_method_to_be_used == 13:
		while True:
			print(f'> The {isnumeric_method} method returns a boolean value of True or False if the string is composed of ONLY either alphabetic or numeric characters. ')
			print()
			user_string = input(enter_string_prompt)
			print()

			print('> Processing ...')
			while counter < random.randint(10, 20):
				print(' ...')
				counter += 1

			print()
			print(f'> Your string: {user_string}')
			print(f'> {isalnum_method} applied:', user_string.isalnum())
			print()

			proceed = input(again_prompt)
			print()
			if proceed.lower() == 'n':
				break

		print()
		proceed = input(choose_another_method_prompt)
		print()
		if proceed.lower() == 'n':
			break

	# len()
	elif string_method_to_be_used == 14:
		while True:
			print(f'> The {len_function} function returns how many characters are in the string. In other words, it measures how long the string is. Whitespace characters and symbols are counted.')
			print()
			user_string = input(enter_string_prompt)
			print()

			print(' Processing ...')
			while counter < random.randint(10, 20):
				print(' ...')
				counter += 1

			print()
			print(f'> Your string: {user_string}')
			print(f'> {len_function} function applied:', len(user_string))
			print()

			proceed = input(again_prompt)
			print()
			if proceed.lower() == 'n':
				break

		print()
		proceed = input(choose_another_method_prompt)
		print()
		if proceed.lower() == 'n':
			break

	# upper()
	elif string_method_to_be_used == 15:
		while True:
			print(f'> The {split_method} method "splits" the string and converts it into a list.')
			print()
			user_string = input(enter_string_prompt)
			print()

			print(' Processing ...')
			while counter < random.randint(10, 20):
				print(' ...')
				counter += 1

			print()
			print(f'> Your string: {user_string}')
			print(f'> {split_method} method applied: ', user_string.split())
			print()

			proceed = input(again_prompt)
			print()
			if proceed.lower() == 'n':
				break

		print()
		proceed = input(choose_another_method_prompt)
		print()
		if proceed.lower() == 'n':
			break				

	# When user enters an invalid value.
	else:
		print(invalid_command_message)
		print()

print('> Goodbye.\n')

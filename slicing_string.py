# This script demonstrate string slicing. User enters a string and the user must enter the correct answer to
# the different stride of the slice of the string.
user_string = ''
mistakes = 0
correct_message = '> Correct!'
incorrect_message = '> Wrong!'
cheat_code_message = '> She\'s the perfect wife!'
cheat_code = 'nikki'
compare_answer_message = '> The correct answer was {}. You\'re answer is: {}'

while True:
    user_string = input('> Input String: ')
    print()
    if user_string.isspace():
        print('> String must contain characters.')
    elif user_string.islower():
        print('String must contain uppercase characters.')
    elif user_string.isupper():
        print('String must contain lowercase characters.')
    elif len(user_string) < 20:
        print('> String must contain at least 20 characters.')
    else:
        break

message_for_user = f'''\
> You have entered: {user_string}
> You must now input the correct string slice with different strides of your string.

> There are 20 levels.\
'''
print(message_for_user)
print()

question = f'> What is the output of your string:\n> {user_string}\n> If it is sliced with'

#  Level 1
string1 = user_string[::1]
user_string1 = input(f'{question} [::1]? ')
if user_string1 == string1:
    print(compare_answer_message.format(string1, user_string1))
    print(correct_message)
    print()
elif user_string1.lower() == cheat_code:
    print(cheat_code_message)
    print()
else:
    print(compare_answer_message.format(string1, user_string1))
    print(incorrect_message)
    print()
    mistakes += 1

# Level 2
if mistakes == 0:
    string2 = user_string[::2]
    user_string2 = input(f'{question} [::2]? ')
    if user_string2 == string2:
        print(compare_answer_message.format(string2, user_string2))
        print(correct_message)
        print()
    elif user_string2.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string2, user_string2))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 3
if mistakes == 0:
    string3 = user_string[::3]
    user_string3 = input(f'{question} [::3]? ')
    if user_string3 == string3:
        print(compare_answer_message.format(string3, user_string3))
        print(correct_message)
        print()
    elif user_string3.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string3, user_string3))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 4
if mistakes == 0:
    string4 = user_string[::4]
    user_string4 = input(f'{question} [::4]? ')
    if user_string4 == string4:
        print(compare_answer_message.format(string4, user_string4))
        print(correct_message)
        print()
    elif user_string4.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string4, user_string4))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 5
if mistakes == 0:
    string5 = user_string[::5]
    user_string5 = input(f'{question} [::5]? ')
    if user_string5 == string5:
        print(compare_answer_message.format(string5, user_string5))
        print(correct_message)
        print()
    elif user_string5.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string5, user_string5))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 6
if mistakes == 0:
    string6 = user_string[::6]
    user_string6 = input(f'{question} [::6]? ')
    if user_string6 == string6:
        print(compare_answer_message.format(string6, user_string6))
        print(correct_message)
        print()
    elif user_string6.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string6, user_string6))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 7
if mistakes == 0:
    string7 = user_string[::7]
    user_string7 = input(f'{question} [::7]? ')
    if user_string7 == string7:
        print(compare_answer_message.format(string7, user_string7))
        print(correct_message)
        print()
    elif user_string7.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string7, user_string7))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 8
if mistakes == 0:
    string8 = user_string[::8]
    user_string8 = input(f'{question} [::8]? ')
    if user_string8 == string8:
        print(compare_answer_message.format(string8, user_string8))
        print(correct_message)
        print()
    elif user_string8.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string8, user_string8))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 9
if mistakes == 0:
    string9 = user_string[::9]
    user_string9 = input(f'{question} [::9]? ')
    if user_string9 == string9:
        print(compare_answer_message.format(string9, user_string9))
        print(correct_message)
        print()
    elif user_string9.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string9, user_string9))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 10
if mistakes == 0:
    string10 = user_string[::10]
    user_string10 = input(f'{question} [::10]? ')
    if user_string10 == string10:
        print(compare_answer_message.format(string10, user_string10))
        print(correct_message)
        print()
    elif user_string10.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string10, user_string10))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 11
if mistakes == 0:
    string11 = user_string[::-1]
    user_string11 = input(f'{question} [::-1]? ')
    if user_string11 == string11:
        print(compare_answer_message.format(string11, user_string11))
        print(correct_message)
        print()
    elif user_string11.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string11, user_string11))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 12
if mistakes == 0:
    string12 = user_string[::-2]
    user_string12 = input(f'{question} [::-2]? ')
    if user_string12 == string12:
        print(compare_answer_message.format(string12, user_string12))
        print(correct_message)
        print()
    elif user_string12.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string12, user_string12))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 13
if mistakes == 0:
    string13 = user_string[::-3]
    user_string13 = input(f'{question} [::-3]? ')
    if user_string13 == string13:
        print(compare_answer_message.format(string13, user_string13))
        print(correct_message)
        print()
    elif user_string13.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string13, user_string13))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 14
if mistakes == 0:
    string14 = user_string[::-4]
    user_string14 = input(f'{question} [::-4]? ')
    if user_string14 == string14:
        print(compare_answer_message.format(string14, user_string14))
        print(correct_message)
        print()
    elif user_string14.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string14, user_string14))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 15
if mistakes == 0:
    string15 = user_string[::-5]
    user_string15 = input(f'{question} [::-5]? ')
    if user_string15 == string15:
        print(compare_answer_message.format(string15, user_string15))
        print(correct_message)
        print()
    elif user_string15.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string15, user_string15))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 16
if mistakes == 0:
    string16 = user_string[::-6]
    user_string16 = input(f'{question} [::-6]? ')
    if user_string16 == string16:
        print(compare_answer_message.format(string16, user_string16))
        print(correct_message)
        print()
    elif user_string16.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string16, user_string16))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 17
if mistakes == 0:
    string17 = user_string[::-7]
    user_string17 = input(f'{question} [::-7]? ')
    if user_string17 == string17:
        print(compare_answer_message.format(string17, user_string17))
        print(correct_message)
        print()
    elif user_string17.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string17, user_string17))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 14
if mistakes == 0:
    string18 = user_string[::-8]
    user_string18 = input(f'{question} [::-8]? ')
    if user_string18 == string18:
        print(compare_answer_message.format(string18, user_string18))
        print(correct_message)
        print()
    elif user_string18.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string18, user_string18))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 19
if mistakes == 0:
    string19 = user_string[::-9]
    user_string19 = input(f'{question} [::-9]? ')
    if user_string19 == string19:
        print(compare_answer_message.format(string19, user_string19))
        print(correct_message)
        print()
    elif user_string19.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string19, user_string19))
        print(incorrect_message)
        print()
        mistakes += 1

# Level 20
if mistakes == 0:
    string20 = user_string[::-10]
    user_string20 = input(f'{question} [::-10]? ')
    if user_string20 == string20:
        print(compare_answer_message.format(string20, user_string20))
        print(correct_message)
        print()
    elif user_string20.lower() == cheat_code:
        print(cheat_code_message)
        print()
    else:
        print(compare_answer_message.format(string20, user_string20))
        print(incorrect_message)
        print()
        mistakes += 1

if mistakes != 0:
    print('> You Lose!')
else:
    print('> You Win! Congratulations!')
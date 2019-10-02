# Initializes a variable named types_of_people with a value of 10, an integer.
types_of_people = 10
# Initializes a variable named x with a value of an f-string or format string with one placeholder with the variable types_of_people.
x = f"There are {types_of_people} types of people."

# Initializes a variable named binary with a value of a string literal "binary".
binary = "binary"
# Initializes a variable named do_not with a value of a string literal "don't".
do_not = "don't"
# Initializes a variable named y with a value of an f-string or format string with two placeholders with the variables binary and do_not respectively.
y = f"Those who know {binary} and those who {do_not}."

# The print() function is called and given an argument of x.
print(x)
# The print() function is called and given an argument of y.
print(y)

# The print() function is called and given an argument of an f-string that has one placeholder with the variable x.
print(f"I said: {x}")
# The print() function is called and given an argument of an f-string that has one placeholder with the variable y.
print(f"I also said: '{y}'")

# Initializes a variable named hilarious with a Boolean value of False.
hilarious = False
# Initializes a variable named joke_evaluation with a value of a string literal "Isn't that joke so funny?! with a placeholder."
joke_evaluation = "Isn't that joke so funny?! {}"

# The print() function is called and given an argument of the variable joke_evaluation with a method invocation of format() that has an argument of hilarious. The value of the variable hilarious is passed to the placeholder of joke_evaluation.
print(joke_evaluation.format(hilarious))

# Initializes a variable named w with a value of a string literal "This is the left side of ..."
w = "This is the left side of ..."
# Initializes a variable named e with a value of a string literal "a string with a right side."
e = "a string with a right side."

# The print() function is called and given an argument of w and e added together, in this case since w and e have values that are strings, they are concatenated, the + sign is for concatenation, not addition.
print(w + e)
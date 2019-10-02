print("I will now count my chickens:")

# The order of precedence is PEMDAS, with Multiplication and Division having the same precedence, and Addition and Subtaction also having the same precedence. If they are both in an expression, they are solved from left to right.

print("Hens", 25.0 + 30.0 / 6.0)
# 25.0 + 5.0
# 30.0

print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)
# 100.0 - 75.0 % 4.0
# 100.0 - 3.0
# 97.0

print("Now I will count the eggs:")

print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)
# 3.0 + 2.0 + 1.0 - 5.0 + 0.0 - 1.0 / 4.0 + 6.0
# 3.0 + 2.0 + 1.0 - 5.0 + 0.0 - 0.25 + 6.0
# 5.0 + 1.0 - 5.0 + 0.0 - 0.25 + 6.0
# 6.0 - 5.0 + 0.0 - 0.25 + 6.0
# 1.0 + 0.0 - 0.25 + 6.0
# 1.0 - 0.25 + 6.0
# 0.75 + 6.0
# 6.75

# Arithmetic Operators have a higher precedence than boolean operators.
print("Is it true that 3.0 + 2.0 < 5.0 - 7.0?")

print(3.0 + 2.0 < 5.0 - 7.0)
# 5.0 < 5.0 - 7.0
# 5.0 < -2.0
# False

print("What is 3 + 2?", 3.0 + 2.0) # 5.0
print("What is 5 - 7?", 5.0 - 7.0) # -2.0

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5.0 > -2.0) # True
print("Is it greater or equal?", 5.0 >= -2.0) # True
print("Is it less or equal?", 5.0 <= -2.0) # False
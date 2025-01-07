# String Formatting



# argument specifiers

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)


# %s and %d
name = 'yuki'
age = 60

print('my name is %s' % name)
print('my name is %s' % age)

# print('my name is %d' % name) ini error karena hanya berlaku untuk integers
print('my name is %d' % age)

print(15*' = ')

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
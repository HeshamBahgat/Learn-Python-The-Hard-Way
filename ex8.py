# string format method call

formatter = "{} {} {} {}"

# number of the arguments in .format must match {} in the variable

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
    "first thoughts!!",
    "that's what is in my mind,",
    "Let's do it,",
    "Python is the key"
))

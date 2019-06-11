types_of_people = 10



"""
1- A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. 
2- These strings may contain replacement fields, which are expressions delimited by curly braces {}. 
3- While other string literals always have a constant value, formatted strings are really expressions evaluated at run time.
"""
people = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"

seprates = f"Those who know {binary} and those who {do_not}"

print(people)
print(seprates)

print(f"I said: {people}")

print(f"I also said: {seprates}'")

hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"


print(joke_evaluation.format(hilarious))

w = "This is the left side of ...."

e = "a string with a right side."

# string concatenation
print(w + e)
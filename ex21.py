
def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b # we can use it to specify the out put of the fuction


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiplay(a, b):
    print(f"MULTIPLAYING {a} * {b}")
    return a * b

def divide (a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Lets do some math with just fuctions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiplay(90, 50)
iq = divide(100, 3)

# A puzzle for extra credit, type it in anyway

print("Here is a puzzle.")

what = add(age, subtract(height, multiplay(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
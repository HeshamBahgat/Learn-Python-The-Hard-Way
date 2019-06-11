

def print_two(*args):
    arge1, arge2 = args
    print(f"arge1: {arge1}, arg2: {arge2}")


# ok, that *args is actually pointless, we can just do this


def print_two_again(arg1, arg2):
    print(f"arge1: {arg1}, arg2: {arg2}")

# this just takes one argument

def print_one(arg1):
    print(f"arg1: {arg1}")

# this takes no argument

def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")

print_two_again("Zed", "Shaw")

print_one("First")

print_none()
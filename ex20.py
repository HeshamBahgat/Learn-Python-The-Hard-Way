from sys import argv

script, input_file = argv

def print_all(f): # create a function so will take the file name, read it and print inside the file
    print(f.read())


def rewind(f): # go back to first character
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file, 'w')
current_file = open(input_file, 'r')


print("First let's print the whole file:\n")
print_all(current_file)


print("Now lets rewind, kind of like a tape.")
rewind(current_file)


print("Lets print three lines:")


current_line = 1
print_a_line(current_line, current_file)


current_line += 1
print_a_line(current_line, current_file)
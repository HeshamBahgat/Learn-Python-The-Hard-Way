from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")


input("?")


print("Opening the file....")

target = open(filename, "w")


print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask to you for three lines")


l1 = input("line 1: ")
l2 = input("line 2: ")
l3 = input("line 3: ")

line = [l1, l2, l3]

print("I'm going to write these to the file.")

for lines in line:
    target.write(lines)
    target.write("\n")

target = open(filename, "r")

for count in range(len(line)):
    print(target.readline())




print("And finally, we close it.")
target.close()



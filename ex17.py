from sys import argv
from os.path import exists

script, file_1, file_2 = argv
print(f"Creating Two Files {file_1} and {file_2}")

# Creating Two files and names of the files will be taken from argv(user-inputs)
file1 = open(file_1, "w")
file2 = open(file_2, "w")

# Take data to write in user's file 1
prompt = ("> ")
print("Write your data", end='')
line1 = input(prompt)
file1.write(line1)
file1.write("\n")

print("Do you want to add more lines?(Y/N)")
answer = input(prompt)
if answer == "Y":
    line2 = input("Please write what do you want to add: ")
    file1.write(line2)
    file1.write("\n")
else:
    print("Nice lets get going")

# copy file 1 to file 2
print("Lets use more methods and copying data form {0} to {1}".format(file_1, file_2))

file1 = open(file_1, "r")
indata = file1.read()

print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist? {exists(file_2)}")

print("Ready, hit RETURN to continue. CTRL-C to abort.")

input()

file2.write(indata)


print("Alright, all done.")


file1.close()
file2.close()

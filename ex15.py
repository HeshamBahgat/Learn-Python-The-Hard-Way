from sys import argv


script, filename = argv
prompt = "> Add Data for the file: "


# txt = open(filename) makes --> file object
txt = open(filename, "r+")
"""
"r"  open a file for reading only
"r+" opens a file for both reading and writing
"rb" open a file for reading only in binary format
"rb+" opens a file for both reading and writing in binary format
"w"  open a file for writing only ## the existing file with the same name will be erased
"a" opens the file for appending

"x" open the file for exclusive creation, falling if the file already exists
"""



print(f"Here's your file {filename}:")

input_1 = input(prompt)
txt.write(input_1)

txt.read()
print(txt)



print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again, "r+")

input_2 = input(prompt)
txt_again.write(input_2)

print(txt_again.read())



ten_things = "Apples Oranges Crows Telephone Light Sugar" # create a string

print("Wait there are not 10 things in that list. let's fix that.")

stuff = ten_things.split(" ") # split all words seprated with a space and create alist

more_stuff = ["day", " Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"] # another list

# create a while loop for the list if less than 10 slots will take elemnts form another list till be 10 slts
while len(stuff) != 10:
    next_one = more_stuff.pop() # will remove the last element iny the list then will crate a vriablee
    print("Adding: " , next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")



print("There we go: ", stuff)
print("Lets do some things with stuff.")

print(stuff[1])
print(stuff[-1])

print(stuff.pop())
join = (" ".join(stuff)) # retrun a strin seprated with space
print(join, type(join))

print("#".join(stuff[3:6])) # retrun a string but first will do slicing the will seprate the elemnts with #


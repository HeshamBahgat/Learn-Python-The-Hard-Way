## Escape Sequence ##

# \newline 	Backslash and newline ignored
# \\ 	Backslash (\)
# \' 	Single quote (')
# \" 	Double quote (")
# \a 	ASCII Bell (BEL)
# \b 	ASCII Backspace (BS)
# \f 	ASCII Formfeed (FF)
# \n 	ASCII Linefeed (LF)
# \r 	ASCII Carriage Return (CR)
# \t 	ASCII Horizontal Tab (TAB)
# \v 	ASCII Vertical Tab (VT)
# \ooo 	Character with octal value ooo 	(1,3)
# \xhh 	Character with hex value hh 	(2,3)



tabby_cat = "\tI'm tabbed in"

persiancat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."


fat_cat= """
I'll do a list:
\t* Cat food
\t^ Fishies
\t^ Catnip\n\t^ Grass
"""

print(tabby_cat)
print(persiancat)
print(backslash_cat)
print(fat_cat)
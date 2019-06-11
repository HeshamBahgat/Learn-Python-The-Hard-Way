import sys



script, input_encoding, error = sys.argv


# will pass the encoding type UTF-8 from the cli cuz of argv
# the default for errors is "strict" and also will be passed via cli

def main(language_file, encoding, errors):
    line = language_file.readline() # reade line by line in the languages.txt that is already avilable with same dir with tge current script

    if line: # if line has something keep going
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip() # removing the whitespace in this case is stripping of the trailing \n
    raw_bytes = next_lang.encode(encoding, errors=errors)  # return an encode version of the string
    cooked_string = raw_bytes.decode(encoding, errors=errors) # return a string decoded from the given bytes

    print(raw_bytes, "<======>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

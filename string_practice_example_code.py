# some advanced string practice

# Going over how quotes work
"This is a string"
'This is also a string'

"This isn't a problem"

# 'This isn't good'
# "She told me "leave, please"."

'She told me "leave, please".'

# "She told me, "don't leave"."
# 'She told me, "don't leave".'
print("She told me, \"don't leave\".")
print("This\nhas\na lot\nof\nline breaks.\n\n")
print("\u2660")

###################################
# find and index

example_string = "banana"
example_string.count("a")
example_string.find("a")
example_string.find("a", 2)
example_string.index("a")
example_string.index("a", 2)

example_string.find("z")
example_string.index("z")

with open("spam_song.txt") as fc:
    spam_song = fc.read()

type(spam_song)
len(spam_song)
spam_song.find("spam")
spam_song[400]
spam_song[400:404]
spam_song[390:414]

# find ALL of the occurrences
spam_song.find("spam", 431)

character_number = 0
spam_locations = []
while character_number < len(spam_song):
    found_spam = spam_song.find("spam", character_number)
    print(found_spam)
    if found_spam == -1:
        break
    spam_locations.append(found_spam)
    character_number = found_spam + 1

print(spam_locations)
len(spam_locations)
spam_song.count("spam")


######################
# starting examples for 4/25
# starting with startswith and endswith

"file_name.txt".endswith(".txt")
"file_name.py".endswith(".txt")

import os

list_of_files = os.listdir()
print(list_of_files)

for filename in list_of_files:
    print(f"let's check to see if {filename} ends with .txt")
    if filename.endswith(".txt"):
        print(f"about to open {filename}")
        with open(filename) as file_connection:
            print(file_connection.read(100))


waitress_lines = []
with open("spam_song.txt") as file_connection:
    for line in file_connection:
        if line.startswith("Waitress"):
            waitress_lines.append(line)

print(waitress_lines)

print("\n".join(waitress_lines))

data_row = ["student", "year", "gpa"]

print(data_row[0] + "," +
      data_row[1] + "," +
      data_row[2])

print(",".join(data_row))

######################################
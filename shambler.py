import os

# Necessary inputs for shambler to work with.
file_path = input("Enter file path: ")
# Verifies if the file path is correct.
if file_path[-1] != "/":
    file_path = file_path + "/"

file_name = input("Enter file name: ")
json_file_name = input("Enter a name for the JSON file: ")
json_key = input("Enter a key for the JSON file: ")


script_path = os.path.realpath(__file__)

# Goes back to the root of the machine to then add the file path to then correctly add it.
going_back = ""
counter5 = 1
while counter5 <= len(script_path.split("/")):
    if counter5 == len(script_path.split("/")):
        going_back = going_back + ".."
    else:
        going_back = "../" + going_back
    counter5 += 1

file_path = going_back + file_path + file_name
print("file_path", file_path)
file = open(file_path)

# Places all lines of original file in a list, checks for correct file name.
original_file_list = []
try:
    with file as f:
        original_file_list = f.readlines()
    f.close()
except FileNotFoundError:
    print(file_name + " was not found, please verify the name or the path of it.")
    quit()

json_file = open("./JSON_Files/" + json_file_name + ".json", "w")


# json_line creates the lines that are going to be placed on the json file.
def json_line(original_line, key):
    new_line = '"' + key + '": "' + original_line + '"'
    return new_line


# Eliminates the new-line character from all the list elements one at a time.
counter1 = 0
while counter1 < len(original_file_list):
    original_file_list[counter1] = original_file_list[counter1][0:len(original_file_list[counter1]) - 1]
    counter1 += 1

# Replaces all the double quotes to single quotes.
counter2 = 0
while counter2 < len(original_file_list):
    new_string = ""
    for letter in original_file_list[counter2]:
        if letter == '"':
            new_string += "'"
        else:
            new_string += letter
    original_file_list[counter2] = new_string
    counter2 += 1

json_file.write("[\n")


counter3 = 0
while counter3 < len(original_file_list):
    # The original file usually is populated with empty elements.
    if original_file_list[counter3] == "":
        counter3 += 1
        continue

    json_file.write("\t{\n")
    json_file.write("\t" + json_line(original_file_list[counter3], json_key) + "\n")
    if counter3 == len(original_file_list)-1:
        json_file.write('\t}\n')
    else:
        json_file.write('\t},\n')
    counter3 += 1

json_file.write("]")
json_file.close()


print(json_file_name + ".json" + " created successfully, placed in the JSON_Files directory.")

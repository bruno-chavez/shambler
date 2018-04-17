original_file_name = input("Enter file name: ")
json_file_name = input("Enter a name for the JSON file: ")
json_key = input("Enter a key for the JSON file: ")


with open(original_file_name) as f:
    original_file_list = f.readlines()

f.close()

json_file = open(json_file_name + ".json", "w")


def json_line(original_line, key):
    new_line = '"' + key + '": "' + original_line + '"'
    return new_line


counter1 = 0
while counter1 < len(original_file_list):
    original_file_list[counter1] = original_file_list[counter1][0:len(original_file_list[counter1]) - 1]
    counter1 += 1

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

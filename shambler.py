import os
from itertools import chain

JSON_EXT = '.json'
JSON_FOLDER = 'JSON_Files'


def shambler(source_file, target_filename, json_key):
    # Places all lines of original file in a list, checks for correct file name.
    source_file_lines = []

    with open(source_file) as f:
        source_file_lines = f.readlines()

    # Replaces all the double quotes to single quotes and strips trailing whitespace and removes empty lines
    source_file_lines = [line.rstrip().replace('\"', '\'')
                         for line in source_file_lines]
    source_file_lines = [line for line in source_file_lines if line]
    json_file = open(target_filename, "w")
    json_file.write("[\n")

    num_lines = len(source_file_lines)
    keys = _resolve_key_list(json_key, num_lines)

    for i, (line, key) in enumerate(zip(source_file_lines, keys)):
        json_file.write("\t{\n")
        json_file.write('\t"{K}": "{V}"\n'.format(K=key, V=line))
        json_file.write('\t}\n' if i == num_lines - 1 else '\t},\n')

    json_file.write("]")
    json_file.close()


def shambler_interactive():
    # Necessary inputs for shambler to work with.
    file_path = input("Enter your input plain text file: ")
    json_file_name = input("Enter a name for the output JSON file: ")
    # User has the option of inputting json_key in the format "key, number, key, number"
    # So that they can specify keys and the number of uses of each key in order.
    json_key = input("Enter a key to use in the JSON file: ")

    # Checking whether the user has input file names, file paths
    # If they are relative, we will let python take care of it.
    file_path = _resolve_relative_file(file_path)
    if not os.path.exists(file_path):
        raise FileNotFoundError('%s was not found.' % file_path)
    json_file_name = _resolve_relative_file(json_file_name, extension=JSON_EXT)

    shambler(file_path, json_file_name, json_key)

    print(json_file_name + " created successfully.")


def _resolve_key_list(json_key_user_input, num_lines):
    if ',' in json_key_user_input:
        # Split user input by commas
        keys = ','.join(json_key_user_input.split(', ')).split(',')
        keys = zip(keys[::2], keys[1::2])

        # Creating a list of each key entry multiplied by the number following it.
        keys = list(chain.from_iterable(
            [[key_pair[0]] * int(key_pair[1]) for key_pair in keys]))

        # Now filling out the list with the last entry if it does not match the number of lines in the source file.
        if len(keys) < num_lines:
            print('You entered %d too few keys, padding with %s' %
                  (abs(len(keys) - num_lines), keys[-1]))
            keys = keys + [keys[-1]] * abs(len(keys) - num_lines)
    else:
        keys = (json_key_user_input, num_lines)
    return keys


def _resolve_relative_file(file_path, extension=''):
    script_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
    # Resolves the json file path to an absolute path within the JSON_Files folder if not already a path
    if os.path.sep not in file_path:
        file_path = os.path.join(script_path, JSON_FOLDER, file_path)
    return file_path + extension


if __name__ == '__main__':
    shambler_interactive()

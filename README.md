`shambler` is a pretty simple Python script, that creates a file with JSON's object format from a specified file.

## Download

Requires Python 3 to be installed on your machine. You can install Python from [here](https://www.python.org/downloads/release/python-365/).

Download the script clicking [here](https://github.com/bruno-chavez/shambler/archive/master.zip), or clone it from a terminal by typing:

```
$ git clone https://github.com/bruno-chavez/shambler.git
```

## Usage

To use `shambler` simply execute the script, the new file will be placed in the JSON_Files directory, which is inside `shambler`'s directory.

```
$ python shambler.py
Enter file path: /home/USER/Desktop
Enter file name: sample.txt
Enter a name for the JSON file: newsample
Enter a key for JSON format: quote

newsample.json created succesfuly, placed in the JSON_Files directory.
```
## Format

`shambler` was made to resist things like double quotes or white spaces, things that normally can get in your way but don't worry about those and let it format those for you.

You can run the sample text on the JSON_Files directory to see what kind of special cases `shambler` can handle, if you find anything that you would like to be added please post an [issue](https://github.com/bruno-chavez/shambler/issues).
## Notes

This is a pretty small project, with limited but hopefully some utility.
Current version: `0.2`

## Contribute

Found an bug or an error? Post it in the [issue tracker](https://github.com/bruno-chavez/shambler/issues).

Want to add an awesome new feature? [Fork](https://github.com/bruno-chavez/shambler/fork) this repository and add your feature, then send a pull request.

## License
The MIT License (MIT)
Copyright (c) 2018 Bruno Chavez

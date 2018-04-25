`shambler` is a pretty simple Python script, that creates a file with JSON's object format from a specified file.

## Download

Requires Python 3 to be installed on your machine. You can install Python from [here](https://www.python.org/downloads/release/python-365/).

Download the file clicking [here](https://github.com/bruno-chavez/shambler/archive/master.zip), or clone it from a terminal:

```
$ git clone https://github.com/bruno-chavez/shambler.git
```

## Usage

To use `shambler` place the file you wish to convert inside the convert directory, the JSON file created will be placed right next to it, after that run the next command on a terminal:

```
$ python shambler.py
Enter file name: sample.txt
Enter a name for the JSON file: newsample
Enter a key for JSON format: quote

newsample.json created succesfuly, placed right next to sample.txt.
```
## Format

`shambler` was made to resist things like double quotes or white spaces, things that normally can get in your way but don't worry about those and let it format those for you.

You can run the sample text on the convert file to see what kind of special cases `shambler` can handle, if you find anything that you would like to be added please post an [issue](https://github.com/bruno-chavez/shambler/issues).
## Notes

This is a pretty small project, with limited but hopefully some utility.
Current version: `0.2`

## Contribute

Found an bug or an error? Post it in the [issue tracker](https://github.com/bruno-chavez/shambler/issues).

Want to add an awesome new feature? [Fork](https://github.com/bruno-chavez/shambler/fork) this repository and add your feature, then send a pull request.

## License
The MIT License (MIT)
Copyright (c) 2018 Bruno Chavez

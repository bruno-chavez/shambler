# Shambler
 `shambler` is a pretty simple Python script, that creates a file with JSON's object format from a specified file.

## Download

Requires Python 3 to be installed on your machine. You can install Python from [here](https://www.python.org/downloads/release/python-365/).

Download the script clicking [here](https://github.com/bruno-chavez/shambler/archive/master.zip), or clone it from a terminal by typing:

```
$ git clone https://github.com/bruno-chavez/shambler.git
```

## Installation
You can run `shambler` via python as detailed below, however from the command line within the top level `shambler` folder you can install it using pip:
```
$ pip install .
```

## Usage

`Terminal`

To interactively use `shambler` via the command line interface (CLI) you can access it using:
```
$ shambler
```

`Python`

To use `shambler` within python simply execute the script, the new file will be placed in the JSON_Files directory, which is inside `shambler`'s directory.

```
$ python shambler.py
Enter your input plain text file: /home/USER/Desktop/sample.txt
Enter a name for the output JSON file: newsample
Enter a key to use in the JSON file: quote

D:\\dev\\shambler\\JSON_Files\\newsample.json created succesfuly.
```
If you place your text file within the `shambler` directory you can also reference it locally or it will automatically check within the JSON_Files folder. Alternatively you can enter absolute file paths as well for either the source text file or the output json file.

```
$ python shambler.py
Enter your input plain text file: sample.txt
Enter a name for the output JSON file: newsample
Enter a key to use in the JSON file: quote

D:\\dev\\shambler\\JSON_Files\\newsample.json created succesfuly.
```


Also feel free to import shambler from within a python script:
```
from shambler import shambler
shambler('sample.txt', 'newsample', 'quote') # this will return the output file path
```


## Format

`shambler` was made to resist things like double quotes or white spaces, things that normally can get in your way but don't worry about those and let it format those for you.

You can run the sample text on the JSON_Files directory to see what kind of special cases `shambler` can handle, if you find anything that you would like to be added please post an [issue](https://github.com/bruno-chavez/shambler/issues).

## Example

If your file looks like this:

`my_file.txt`
```
Lorem
ipsum
dolor
sit
```

And you run shambler from python like this:
```
$ python
>>> from shambler import shambler
>>> shambler('my_file.txt', 'my_output', 'new_key')
# 'resulting file path gets returned'
```
Your final output json file will look like this:

`my_output.json`
```
[
	{
	"new_key": "Lorem"
	},
	{
	"new_key": "ipsum"
	},
	{
	"new_key": "dolor"
	},
	{
	"new_key": "sit"
	}
]
```
You can also use a comma separated list of keys and number of uses of that key:
 And you run shambler from python like this:
```
$ python
>>> from shambler import shambler
>>> shambler('my_file.txt', 'my_output', 'key1,2,key2,2')
# 'resulting file path gets returned'
```
`my_output.json`
```
[
	{
	"key1": "Lorem"
	},
	{
	"key1": "ipsum"
	},
	{
	"key2": "dolor"
	},
	{
	"key2": "sit"
	}
]
```
If you enter too many or too few it will appropriately fill in with the last key value or cut off the key values to the length values in your text file.
## Notes

This is a pretty small project, with limited but hopefully some utility.
Current version: `0.2`

## Contribute

Found an bug or an error? Post it in the [issue tracker](https://github.com/bruno-chavez/shambler/issues).

Want to add an awesome new feature? [Fork](https://github.com/bruno-chavez/shambler/fork) this repository and add your feature, then send a pull request.

### Testing
You can install it in development mode using
```
$ pip install -e .
```

To run the `test suite` while in the top level `shambler` directory you can run:
```
$ python setup.py test
```
or 
```
$ python -m unittest discover .
```
## License
The MIT License (MIT)
Copyright (c) 2018 Bruno Chavez

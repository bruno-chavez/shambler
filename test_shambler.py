import os
import sys
from unittest import TestCase
from subprocess import Popen, PIPE
from shambler import shambler

json_dir = 'JSON_Files'
json_file = 'sample.txt'
json_file_simple = 'simple_sample.txt'
json_file_short = 'short_sample.txt'
json_file_tabbed = 'tabbed_sample.txt'
test_file_name = 'test_normal_run'
json_key = 'new'


class TestShamblerPython(TestCase):
    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            shambler('doesnt_exist.txt',
                     test_file_name,
                     json_key)

    def test_missing_path(self):
        with self.assertRaises(FileNotFoundError):
            shambler(os.path.join('//not_existing//dir', json_file),
                     test_file_name,
                     json_key)

    def test_missing_relative_folder(self):
        with self.assertRaises(FileNotFoundError):
            shambler(os.path.join('json_dir', json_file),
                     test_file_name,
                     json_key)

    def test_empty_json_filename(self):
        with self.assertRaises(IOError):
            shambler(json_file,
                     '',
                     json_key)


class TestShamblerCVSKeyEntry(TestCase):
    @classmethod
    def setUpClass(cls):
        short_file_path = os.path.join(json_dir, json_file_short)
        simple_file_path = os.path.join(json_dir, json_file_simple)

        with open(short_file_path, 'w') as f:
            f.writelines('\n'.join(['%s%d' % ('value', i) for i in range(1, 5)]))
        with open(simple_file_path, 'w') as f:
            f.write('one_line_example')
        cls.fixtures = [short_file_path, simple_file_path]

    @classmethod
    def tearDownClass(cls):
        for file_path in cls.fixtures:
            os.remove(file_path)

    def test_simple_exact_keys(self):
        output_file = shambler(json_file_simple,
                               test_file_name,
                               'key1,1')
        with open(output_file, 'r') as output_contents:
            self.assertEqual(output_contents.read(),
                             '[\n\t{\n\t"key1": "one_line_example"\n\t}\n]')
        os.remove(output_file)

    def test_simple_proper_key_too_many(self):
        output_file = shambler(json_file_simple,
                               test_file_name,
                               'key1,4')
        with open(output_file, 'r') as output_contents:
            self.assertEqual(output_contents.read(),
                             '[\n\t{\n\t"key1": "one_line_example"\n\t}\n]')
        os.remove(output_file)

    def test_simple_zero_len_key(self):
        output_file = shambler(json_file_simple,
                               test_file_name,
                               'key1,0')
        with open(output_file, 'r') as output_contents:
            self.assertEqual(output_contents.read(),
                             '[\n\t{\n\t"key1": "one_line_example"\n\t}\n]')
        os.remove(output_file)

    def test_simple_negative_len_key(self):
        output_file = shambler(json_file_simple,
                               test_file_name,
                               'key1,-4')
        with open(output_file, 'r') as output_contents:
            self.assertEqual(output_contents.read(),
                             '[\n\t{\n\t"key1": "one_line_example"\n\t}\n]')
        os.remove(output_file)

    def test_simple_many_keys(self):
        output_file = shambler(json_file_simple,
                               test_file_name,
                               'key1,2,key2,5')
        with open(output_file, 'r') as output_contents:
            self.assertEqual(output_contents.read(),
                             '[\n\t{\n\t"key1": "one_line_example"\n\t}\n]')
        os.remove(output_file)

    def test_short_one_key(self):
        output_file = shambler(json_file_short,
                               test_file_name,
                               'key1')
        with open(output_file, 'r') as output_contents:
            self.assertEqual(output_contents.read().count('key1'), 4)
        os.remove(output_file)

    def test_short_one_key_with_len(self):
        output_file = shambler(json_file_short,
                               test_file_name,
                               'key1,1')
        with open(output_file, 'r') as output_contents:
            self.assertEqual(output_contents.read().count('key1'), 4)
        os.remove(output_file)

    def test_short_too_many_keys(self):
        output_file = shambler(json_file_short,
                               test_file_name,
                               'key1,2,key2,5')
        with open(output_file, 'r') as output_contents:
            contents = output_contents.read()
            self.assertEqual(contents.count('key1'), 2)
            self.assertEqual(contents.count('key2'), 2)
        os.remove(output_file)

    def test_short_two_keys_first_key_long(self):
        output_file = shambler(json_file_short,
                               test_file_name,
                               'key1,5,key2,5')
        with open(output_file, 'r') as output_contents:
            self.assertEqual(output_contents.read().count('key1'), 4)
        os.remove(output_file)

    def test_short_three_keys_1_short(self):
        output_file = shambler(json_file_short,
                               test_file_name,
                               'key1,1,key2,1, key3,1')
        with open(output_file, 'r') as output_contents:
            contents = output_contents.read()
            self.assertEqual(contents.count('key1'), 1)
            self.assertEqual(contents.count('key2'), 1)
            self.assertEqual(contents.count('key3'), 2)
        os.remove(output_file)


class TestShamblerCLI(TestCase):
    cli_entry_point = 'shambler'

    def run_cli(self, *cli_line_inputs):
        process = Popen([self.cli_entry_point], stdout=PIPE, stdin=PIPE)
        return process.communicate('\n'.join(cli_line_inputs).encode('utf-8'))[0].decode('utf-8')

    def test_normal_run(self):
        """ Makes sure the ouput path from shambler output is in the printout
            from the CLI.
                Note: Had to use lower() just in case the drive letter is not capitalized.             
                E.G. - 
                    'D:\\dev\\shambler\\JSON_Files\\test_normal_run.json created successfully.'
                    'd:\\dev\\shambler\\JSON_Files\\test_normal_run.json created successfully.'
        """
        expected_path = shambler(json_file, test_file_name, json_key)
        os.remove(expected_path)
        expected_line = '%s created successfully.'
        self.assertIn(str.lower(expected_line % expected_path),
                      str.lower(self.run_cli(json_file, test_file_name, json_key)))
        os.remove(expected_path)

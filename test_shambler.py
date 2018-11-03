from unittest import TestCase
import os
from subprocess import Popen, PIPE


json_dir = 'JSON_Files'
json_file = 'sample.txt'
json_key = 'new'


class TestShamblerPython(TestCase):

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            shambler.shambler(json_dir,
                              'doesnt_exist.txt',
                              'test_missing_file',
                              json_key)

    def test_missing_path(self):
        with self.assertRaises(FileNotFoundError):
            shambler.shambler('no_folder',
                              json_file,
                              'test_missing_path',
                              json_key)

    def test_empty_json_filename(self):
        with self.assertRaises(FileNotFoundError):
            shambler.shambler('no_folder',
                              json_file,
                              '',
                              json_key)


class TestShamblerCLI(TestCase):
    cli_entry_point = 'shambler'
    test_file_name = 'test_normal_run'

    def tearDown(self):
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name + '.json')

    def run_cli(self, *cli_line_inputs):
        process = Popen([self.cli_entry_point], stdout=PIPE, stdin=PIPE)
        return process.communicate('\n'.join(cli_line_inputs))[0]

    def test_normal_run(self):
        self.assertEquals(self.run_cli([json_file, json_dir, self.test_file_name, json_key]),
                          '%s created successfully, placed in the JSON_Files directory.' % self.test_file_name)

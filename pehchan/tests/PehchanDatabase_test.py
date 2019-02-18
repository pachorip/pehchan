import unittest
import os
import shutil
from pehchan.PehchanDatabase  import PehchanDatabase

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','pehchan_database')
class TestOptions:
    def __init__(self, output_directory, input_files, threads,kmers,verbose):
        self.kmers = kmers
        self.threads = threads
        self.input_files = input_files
        self.output_directory = output_directory
        self.verbose = verbose


class TestPehchanDatabase(unittest.TestCase):

    def test_create_directory(self):
        p=PehchanDatabase(TestOptions('output_directory','input_files',1,11,True))
        p.run()
        self.assertTrue(os.path.exists('output_directory'))
        shutil.rmtree('output_directory')

import unittest
import os
import shutil
from pehchan.PehchanDatabase  import PehchanDatabase
from pehchan.Fasta import Fasta
test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','pehchan_database')
class TestOptions:
    def __init__(self, output_directory, input_files, threads,kmerlength,verbose, sketch_size):
        self.kmerlength = kmerlength
        self.threads = threads
        self.input_files = input_files
        self.output_directory = output_directory
        self.verbose = verbose
        self.sketch_size = sketch_size

class TestPehchanDatabase(unittest.TestCase):

    def test_create_directory(self):
        if os.path.exists('output_directory'):
            shutil.rmtree('output_directory')
        p=PehchanDatabase(TestOptions('output_directory',[os.path.join(data_dir,'input.fa')],1,11,True, 2))
        p.run()
        self.assertTrue(os.path.exists('output_directory'))
        shutil.rmtree('output_directory')


    def test_kmer_extraction(self):
        if os.path.exists('output_directory'):
            shutil.rmtree('output_directory')
        p=PehchanDatabase(TestOptions('output_directory',[os.path.join(data_dir,'input.fa')],1,4,True, 6))
        p.run()
        i=os.path.join(data_dir,'input.fa')
        f=Fasta({'AAAA': 2, 'CAAA': 1, 'CCAA': 1, 'CCCA': 1, 'CCCC': 2},i)
        self.assertEqual(p.fastas[i].kmers,f.kmers)

    def test_order_kmer_by_freq(self):
        if os.path.exists('output_directory'):
            shutil.rmtree('output_directory')
        p=PehchanDatabase(TestOptions('output_directory',[os.path.join(data_dir,'input.fa')],1,4,True, 6))
        f = p.order_kmer_by_freq({'AAAA': 2, 'CAAA': 1, 'CCAA': 1, 'CCCA': 1, 'CCCC': 2})
        self.assertEqual(f,{2 : ['AAAA', 'CCCC'], 1 : ['CAAA', 'CCAA','CCCA']})

        

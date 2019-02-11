import unittest
import os
import shutil
from pehchan.Kmers  import Kmers

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','kmers')


class TestKmers(unittest.TestCase):

    def test_kmer_normal(self):
        k = Kmers(os.path.join(data_dir,'input.fa'))
        kmers = k.extract_kmers()
        self.assertEqual(kmers,{'ACGT':5,'AAAA':10})
        

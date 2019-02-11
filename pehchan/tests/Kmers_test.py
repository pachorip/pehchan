import unittest
import os
import shutil
from pehchan.Kmers  import Kmers

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','kmers')


class TestKmers(unittest.TestCase):

    def test_kmer_normal(self):
        k = Kmers(os.path.join(data_dir,'input.fa'),4)
        kmers = k.extract_kmers()
        self.assertEqual(kmers,{'AAAA': 2, 'CAAA': 1, 'CCAA': 1, 'CCCA': 1, 'CCCC': 2})

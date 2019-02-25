import os
import sys
from pehchan.Kmers  import Kmers
from pehchan.Fasta import Fasta
class PehchanDatabase:
    def __init__(self,options):
        self.kmerlength = options.kmerlength
        self.threads = options.threads
        self.input_files = options.input_files
        self.output_directory = options.output_directory
        self.verbose = options.verbose
        self.fastas = {}

        if os.path.exists(self.output_directory):
             print(
             "The output directory already exists, "
             "please choose another name: "
             + self.output_directory)
             sys.exit(1)

        else:
            os.makedirs(self.output_directory)

    def run(self):

        for i in self.input_files:
            k = Kmers(i,self.kmerlength)
            kmers = k.extract_kmers()
            f = Fasta(kmers,i)
            self.fastas[i] = f

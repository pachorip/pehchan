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
        self.fastas = self.populate_fasta_kmers()
        self.sketch_size = options.sketch_size

        if os.path.exists(self.output_directory):
             print(
             "The output directory already exists, "
             "please choose another name: "
             + self.output_directory)
             sys.exit(1)

        else:
            os.makedirs(self.output_directory)

    def populate_fasta_kmers(self):
        fastas = {}
        for i in self.input_files:
            k = Kmers(i,self.kmerlength)
            kmers = k.extract_kmers()
            f = Fasta(kmers,i)
            fastas[i] = f

        return fastas

    def order_kmer_by_freq(self, kmer_frequencies):
        frequencies_to_kmers = {}
        for kmer,kmer_frequency in kmer_frequencies.items():
            if kmer_frequency in frequencies_to_kmers:
                frequencies_to_kmers[kmer_frequency].append(kmer)
            else:
                frequencies_to_kmers[kmer_frequency] = [kmer]
        return frequencies_to_kmers



    def run(self):
        for f in self.input_files:
            frequencies_to_kmers = self.order_kmer_by_freq(self.fastas[f].kmers)
            self.fastas[f].frequencies_to_kmers = frequencies_to_kmers

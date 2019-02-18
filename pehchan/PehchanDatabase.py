import os
import sys
from pehchan.Kmers  import Kmers
class PehchanDatabase:
    def __init__(self,options):
        self.kmers = options.kmers
        self.threads = options.threads
        self.input_files = options.input_files
        self.output_directory = options.output_directory
        self.verbose = options.verbose
        if os.path.exists(self.output_directory):
             print(
             "The output directory already exists, "
             "please choose another name: "
             + self.output_directory)
             sys.exit(1)

        else:
            os.makedirs(self.output_directory)

    def run(self):
        pass

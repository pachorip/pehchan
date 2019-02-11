from Bio import SeqIO
class Kmers:
    def __init__(self, input_fasta,k):
        self.input_fasta = input_fasta
        self.k = k

    def extract_kmers(self):
        kmers={}
        for record in SeqIO.parse(self.input_fasta, "fasta"):
            seq = record.seq
            end = len(seq) - self.k+1
            kmer_sequences = [str(seq[i:i+self.k]) for i in range(0,end) ]


            for i,k in enumerate(kmer_sequences):
                if k in kmers:
                    kmers[k]+=1
                else:
                    kmers[k]=1
        return kmers
        

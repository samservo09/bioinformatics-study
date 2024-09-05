from DNAToolkit import *
import random

# generate random string
randDNAstr = ''.join([random.choice(nucleotides)
                      for nuc in range(50)])

DNAstr = validateDNAseq(randDNAstr)
print(countNucFreq(DNAstr))

def transcription(seq):
    return seq.replace("T", "U") 
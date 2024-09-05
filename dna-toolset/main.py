from DNAToolkit import *
import random

# generate random string
randDNAstr = ''.join([random.choice(nucleotides)
                      for nuc in range(50)])

DNAstr = validateDNAseq(randDNAstr)

# print out results
print(f"\nSequence: {DNAstr}\n")
print(f"[1] + Sequence Length: {len(DNAstr)}\n")
print(f"[2] + Nucleotide Frequency: {countNucFreq(DNAstr)}\n")
print(f"[3] + DNA/RNA Transcription: {transcription(DNAstr)}\n")
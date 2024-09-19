import collections # for shortcut of freq count

# List of 4 nucleotides
nucleotides = ["A", "C", "G", "T"] # Adenine, Cystosine, Guanine, Thymine
DNA_ReverseComplement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

# Bioinformatics Functions

# Validate sequence function to check if it is a DNA string
def validateDNAseq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in nucleotides:
            return False
    return tmpseq

# Count nucleotide frequency 
def countNucFreq(seq):
    # tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    # for nuc in seq:
    #     tmpFreqDict[nuc] += 1
    # return tmpFreqDict
    return dict(collections.Counter(seq))

# DNA to RNA Transcription
def transcription(seq):
    return seq.replace("T", "U") # replace thymine with uracil

# DNA Reverse Complement
def reverse_complement(seq):
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]

# Count protein sequence
def count_protein(seq):
    return len(seq)
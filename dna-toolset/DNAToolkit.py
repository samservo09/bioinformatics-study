import collections # for shortcut of freq count

# List of 4 nucleotides
nucleotides = ["A", "C", "G", "T"] # Adenine, Cystosine, Guanine, Thymine

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

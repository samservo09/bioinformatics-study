import streamlit as st
from DNAToolkit import *
import random

# Generate random DNA string
def generate_random_dna_string(length):
    nucleotides = "ATCG"
    return ''.join([random.choice(nucleotides) for _ in range(length)])

# Validate DNA sequence and count nucleotide frequencies
def process_dna_string(dna_string):
    validated_dna = validateDNAseq(dna_string)
    if validated_dna:
        nuc_freq = countNucFreq(validated_dna)
        return nuc_freq
    else:
        return "Invalid DNA sequence. Please ensure it only contains 'A', 'T', 'C', and 'G'."

# Streamlit app
def main():
    st.title("DNA Sequence Analysis")

    # Buttons for manual entry, random generation, and file upload
    if st.button("Generate Random DNA Sequence"):
        random_length = st.number_input("Enter the desired length of the random sequence:", min_value=1, max_value=1000, value=50)
        dna_input = generate_random_dna_string(random_length)

    elif st.button("Manual Entry"):
        dna_input = st.text_input("Enter a DNA sequence (e.g., 'ATCGGCAT'):")

    if st.button("Upload File"):
        uploaded_file = st.file_uploader("Choose a DNA sequence file")
        if uploaded_file is not None:
            dna_input = uploaded_file.read().decode()

    # Process DNA sequence and display results
    st.subheader("Analyze DNA Sequence")
    if st.button("Analyze"):
        results = process_dna_string(dna_input)
        if results:
            st.success("Nucleotide Frequencies:")
            st.table(results)
        else:
            st.error(results)

if __name__ == "__main__":
    main()
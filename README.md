# Protein Sequence Retrieval Script using Biopython
This script is designed to retrieve protein sequences from the NCBI database using their unique protein IDs and save them in FASTA format. It utilizes the Biopython library to interact with the NCBI Entrez database and handle biological sequence data.

## Goal
The goal of this script is to automate the process of retrieving protein sequences based on their protein IDs and saving them in FASTA format. It reads protein IDs from input files, performs an online search to retrieve the sequences, and then saves the sequences in separate FASTA files.

## Prerequisites
- Python 3.x
- Biopython library (Install using `pip install biopython`)

## How to Use
1. **Ensure the 'fasta_files' Directory:**
   The script expects a directory named 'fasta_files' to be present in the same location as the script. If this directory doesn't exist, create it manually.

2. **Prepare Protein ID Files:**
   Create one or more text files containing protein IDs, with each ID on a separate line. Name these files with the pattern '*_proteinID.txt' (e.g., 'sample_proteinID.txt'). Place these files in the same directory as the script.

3. Set Your Email:
   Open the script file (`retrieve_protein_sequences.py`) in a text editor and locate the line: `Entrez.email = 'your_email@example.com'`. Replace 'your_email@example.com' with your own email address. This email is required for NCBI Entrez access.

4. **Run the Script:**
   Open a terminal or command prompt and navigate to the directory containing the script. Run the script using the command: `python retrieve_protein_sequences.py`

5. **Observe Progress and Results:**
   The script will show progress using a progress bar for each input file. It will fetch the sequences using the protein IDs from the input files and save them in the 'fasta_files' directory. If a sequence file already exists, it will be skipped.

## Output
The retrieved protein sequences will be saved as separate FASTA files in the 'fasta_files' directory. Each input protein ID file will correspond to an output FASTA file containing the sequences.

## Note
- The script assumes that you have the necessary permissions to access the NCBI Entrez database and retrieve protein sequences.


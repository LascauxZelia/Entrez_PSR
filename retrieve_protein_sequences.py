#!/usr/bin/env python3

# Import necessary libraries
from Bio import Entrez
from Bio import SeqIO
import glob
import pandas as pd
from tqdm import tqdm
import os

# Ask the user to input their email address
user_email = input("Enter your email address for NCBI Entrez access: ")

# Set the provided email as the Entrez email
Entrez.email = user_email

# Find all files ending with "_proteinID.txt" in the current directory
id_files = glob.glob('*_proteinID.txt')

# Inform the user about the requirement of a 'fasta_files' directory in the current working directory
print("Directory 'fasta_files' must exist in CWD!")

# Iterate through each protein ID file
for id_file in tqdm(id_files):
    # Generate the output FASTA filename from the input protein ID filename
    out_name = id_file[:-14] + '.fasta'
    
    # Check if the output file already exists in the 'fasta_files' directory
    if not os.path.isfile('./fasta_files/' + out_name):
        print('FASTA file %s does not exist. Retrieving and saving...' % out_name)
        
        # Read the protein IDs from the current file into a DataFrame
        df_id_file = pd.read_csv(id_file)
        
        # Extract the list of protein IDs from the DataFrame
        id_list = list(df_id_file['protein_id'])
        
        # Perform an online search using the protein IDs to obtain search results
        search_results = Entrez.read(Entrez.epost("protein", id=",".join(id_list)))
        
        # Extract WebEnv and QueryKey from search results
        webenv = search_results["WebEnv"]
        query_key = search_results["QueryKey"]
        
        # Fetch the protein sequences using the retrieved information
        handle = Entrez.efetch(db='protein', rettype='fasta', retmode='text', query_key=query_key, webenv=webenv)
        
        # Parse the fetched sequences and save them to the output FASTA file
        seq_list = [rec for rec in SeqIO.parse(handle, 'fasta')] 
        SeqIO.write(seq_list, './fasta_files/' + out_name, 'fasta')
        
        # Close the handle after retrieving and saving sequences
        handle.close()
    else:
        # Inform the user if the output file already exists and skip processing
        print('FASTA file %s exists. Skipping...' % out_name)

# Print a message when all files have been processed
print('Done!')

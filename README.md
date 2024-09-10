# SpyCag
SpyCag: CagA and CM Motif Scanner SpyCag is a Python-based tool designed to scan Cytotoxin-associated gene A (CagA) sequences for EPIYA, and CagA multimerization (CM) motifs from amino acid sequences in a FASTA file. It identifies these key motifs in sequences related to Helicobacter pylori and outputs the results in a user-friendly format.
# Features

EPIYA Motif Identification: Detects the EPIYA motif within the CagA sequence.
CM Motif Detection: Locates the FPL motif followed by 12 additional characters.
Customizable Input and Output: Allows the user to specify input FASTA files and output result files.

# Requirements
Python 3

# Required Python packages:
argparse
pyfastx
re
argcomplete

# Usage
Command Line Arguments
-i, --input: Path to the input amino acid FASTA file.
-o, --output: Path to the output file where results will be saved.

Example Command
python SpyCag.py -i input_sequences.faa -o results.txt
This will scan the provided input_sequences.faa file for CagA, EPIYA, and FPL motifs and save the results in results.txt.


# Example Output
The script will generate output in the following format:

Sequence Name: Seq1
KNFSDIVTVEPIYA...AVSEAKNNNNNNNNNNFPLKTQPALKTGFEVDAFLS
---------EPIYA...   120-134
---------------------------------FPLKTQPALKTGF 200-212
--------------------------------------------------

EPIYA and CM motifs are aligned using dashes, and the positions are displayed relative to the CagA sequences.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Contributing
Feel free to fork the repository, submit pull requests, or raise issues. Contributions are always welcome!

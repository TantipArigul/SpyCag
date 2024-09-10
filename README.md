# SpyCag
**SpyCag** is a Python-based tool designed to scan Cytotoxin-associated gene A (CagA) sequences for EPIYA, and CagA multimerization (CM) motifs from amino acid sequences in a FASTA file. It identifies these key motifs in sequences related to _Helicobacter pylori_ and outputs the results in a user-friendly format.
### Features
|Features|Descriptions|
|---|---|
|EPIYA Motif Identification | Detects the EPIYA motif within the CagA sequence|
|CM Motif Detection| Locates the CM motif within the CagA sequence|

Customizable Input and Output: Allows the user to specify input FASTA files and output result files.

### Requirements
Python 3.5 or later

### Required Python packages:
pyfastx

### Usage
```
usage: SpyCag.py [-h] -i INPUT -o OUTPUT

Scan CagA type and CM motif from a FASTA file.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input Amino acid FASTA file.
  -o OUTPUT, --output OUTPUT
                        Output file to save results.


Example:

python SpyCag.py -i input_sequences.faa -o results.txt
```
This will scan the provided input_sequences.faa file for CagA, EPIYA, and CM motifs and save the results in results.txt.


### Example Output
The script will generate output in the following format:
```
Sequence Name: Seq1
KNFSDIVTVEPIYA...AVSEAKNNNNNNNNNNFPLKTQPALKTGFEVDAFLS
---------EPIYA...   120-134
---------------------------------FPLKTQPALKTGF 200-212
--------------------------------------------------
```
EPIYA and CM motifs are aligned using dashes, and the positions are displayed relative to the CagA sequences.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing
Feel free to fork the repository, submit pull requests, or raise issues. Contributions are always welcome!

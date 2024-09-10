import argparse
import argcomplete
import pyfastx as px
import re

# Define the function to scan motifs
def scan_cagA_type_and_cm_motif(input_file, output_file):
    # Define input parameters
    beg_aa = "KNFSDI"
    end_aa = "AVSEAK"
    epiya = "EP.Y[AT]"
    fpl_motif = "FPL"  # Define the "FPL" motif

    # Regular expressions for matching
    cag = re.compile(f'{beg_aa}.+?{end_aa}')
    epiya_rex = re.compile(f'{epiya}')
    fpl_rex = re.compile(f'{fpl_motif}.{{12}}')  # "FPL" followed by 12 characters

    # Open the output file to write results
    with open(output_file, 'w') as out:
        # Parse the FASTA file
        fa = px.Fastx(input_file)
        
        # Loop through the sequences in the FASTA file
        for name, seq in fa:
            # Find the CagA motif sequence
            m = cag.search(seq)
            if m:
                cagMotifSeq = m.group(0)
                cagMotifStart = m.start()
                
                # Store motifs in a list (for both EPIYA and FPL)
                motif_list = []
                
                # Search for EPIYA motifs within the CagA motif
                for r in epiya_rex.finditer(seq):
                    eseq = r.group(0)
                    estart = r.start() - cagMotifStart
                    eend = r.end() - cagMotifStart
                    cagMotifEach = seq[r.start():r.start()+14]
                    motif_list.append((estart, cagMotifEach, r.start(), r.start() + 14))  # Store EPIYA motif info
                
                # Search for FPL followed by 12 characters
                for fpl in fpl_rex.finditer(seq):
                    fpl_seq = fpl.group(0)
                    fpl_start = fpl.start() - cagMotifStart
                    fpl_end = fpl.end() - cagMotifStart
                    motif_list.append((fpl_start, fpl_seq, fpl.start(), fpl.start() + len(fpl_seq)))  # Store FPL motif info
                
                # Only proceed if we have found any EPIYA or FPL motifs
                if motif_list:
                    out.write(f"Sequence Name: {name}\n")
                    out.write(f"{cagMotifSeq}\n")
                    
                    # Sort motifs by their start positions
                    motif_list.sort(key=lambda x: x[0])
                    
                    # Print motifs in order to the output file
                    for start, motif, real_start, real_end in motif_list:
                        out.write(("-" * start) + motif + f" {real_start}-{real_end}\n")
                    
                    out.write("-" * 50 + "\n")  # Separator for clarity
# Handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description='Scan CagA type and CM motif from a FASTA file.')
    parser.add_argument('-i', '--input', required=True, help='Input Amino acid FASTA file.', type=str)
    parser.add_argument('-o', '--output', required=True, help='Output file to save results.', type=str)

    # Enable tab completion
    argcomplete.autocomplete(parser)
    
    args = parser.parse_args()

    # Run the scanning function
    scan_cagA_type_and_cm_motif(args.input, args.output)

if __name__ == "__main__":
    main()

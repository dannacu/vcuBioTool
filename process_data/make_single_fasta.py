#
# make_single_fasta.py
#
# author: C. Dan Nacu
#
#


import os
import re

def make_singlefasta(directory):

    path_to_file = directory

    out_file = open((directory + 'reads.fasta'), 'w')

    for file in os.listdir(directory):
        if file.endswith(".seq"):
            read_file = open((path_to_file + file), 'r')
            for line in read_file.readlines():
                line = line.strip()
                if (line.startswith(">")):
                    type = re.search('[RF]_', line)
                    type = type.group(0)
                    split_line = re.split('[RF]_', line)
                    out_file.write(split_line[0] + "." + type.strip('_') + "\n")
                else:
                    out_file.write(line + "\n")

# TODO quality checking on FASTQ
# TODO Conver QC FASTQ to single FASTA
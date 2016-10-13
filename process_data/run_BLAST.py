#
# run_blast.py
#

import subprocess

# makeblastdb -in <FILE TO MAKE DATABASE FROM> -dbtype <prot OR nucl> -out <OUTPUT NAME>
def make_blast_db(file_path, db_type, output_name):
    subprocess.call(["makeblastdb", "-in", file_path, "-dbtype", db_type, "-out", output_name])

# blast<p/n> -query <UNKNOWN SEQUENCE FASTA> -db <DATABASE OF INTEREST> -evalue <EVALUE???> -out <OUTPUT FILE NAME>
def blast(query_file_path, db_type, database_file_path, evalue, out_file_path):
    blast_command = "blast"
    if (db_type == 'p' or db_type == 'P'):
        blast_command += 'p'
    else:
        blast_command += 'n'
    subprocess.call([blast_command, "-query", query_file_path, "-db", database_file_path, "-evalue", evalue, "-out", out_file_path])

# this one does both to save time
def database_then_blast(file_for_database_path, query_file_path, db_type, evalue, database_output_name, out_file_path):
    subprocess.call(["makeblastdb", "-in", file_for_database_path, "-dbtype", db_type, "-out", database_output_name])
    blast_command = "blast"
    if (db_type == 'p' or db_type == 'P'):
        blast_command += 'p'
    else:
        blast_command += 'n'
    subprocess.call(
        [blast_command, "-query", query_file_path, "-db", database_output_name, "-evalue", evalue, "-out", out_file_path])

# TODO BLAST output must be readable by analysis tests and tree software


import subprocess

def calc_distances(file):
    num_files = 0
    sum_length = 0
    read_file = open(file, 'r')
    for line in read_file:
        if line.startswith(">"):
            num_files += 1
            continue
        else:
            sum_length += len(line.strip())
    if (((sum_length/num_files) - 1000) < 0):
        return [0, ((sum_length/num_files) + 1000)]
    else:
        return [(((sum_length / num_files)) - 1000), ((sum_length / num_files) + 1000)]



def run_formcon(fasta_file_path, distances):
    subprocess.Popen('formcon', fasta_file_path, distances[0], distances[1])

#
def run_cap3(fasta_file_path, contraint_file_path):
    subprocess.Popen('cap3', fasta_file_path, contraint_file_path)





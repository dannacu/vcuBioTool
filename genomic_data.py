import re


# Requires at least inclusion of the genomic file.
class genomic_data:
    type = 'N'
    count = 0
    file = ""

    def __init__(self, type, count, file):
        self.type = type
        self.count = count
        self.file = file


    def __init__(self, type, file):
        self.type = type
        self.file = file

    def __init__(self, file):
        self.file = file

    # Finds out if file type is DNA RNA or PROTEIN
    # Operation can be quite expensive.
    # Recommended for user to just include type.
    def get_type(self):
        file = open(self.file, 'r')
        for line in file:
            line.strip()
            if line.startswith(">"):
                continue
            else:
                answer = re.match(r'.[BDEFHIJKLMNOPQRSTVWXYZ]', line)
                if (answer == null):
                    answer = re.match(r'.[U]', line)
                    if (answer == null):
                        continue
                    else:
                        return "RNA"
                else:
                    return "Protein"
        return "DNA"

    # Find number of reads in fasta file.
    def get_count(self):
        count = 0
        file = open(self.file, 'r')
        for line in file:
            line.strip()
            if line.startswith(">"):
                count += 1
        return count


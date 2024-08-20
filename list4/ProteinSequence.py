class ProteinSequence:
    def __init__(self, entry, entry_name, protein_names, OS, OX, gene, PE, SV):
        try:
            OX = float(OX)
            PE = float(PE)
            SV = float(SV)

        except:
            raise TypeError("OX, PE and SV parameters must be numbers")

        try:
            entry = str(entry)
            entry_name = str(entry_name)
            protein_names = str(protein_names)
            OS = str(OS)
            gene = str(gene)
        except:
            raise TypeError("entry, entry_name, protein_names, OS and gene must be of type String")

        self.entry = entry
        self.entry_name = entry_name
        self.protein_names = protein_names
        self.OS = OS
        self.OX = OX
        self.gene = gene
        self.PE = PE
        self.SV = SV

    def fasta_to_prot_seq(fasta_file):
        print("notin it just wont stop saying theres an error if i dont write anyhing here")
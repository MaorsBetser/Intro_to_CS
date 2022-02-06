
import sys

def next_gene(i,s):
    start_gene = s.find('ATG',i)
    if start_gene != -1:
        for i in range(start_gene,len(s),3):
            if s[i:i+3] == 'TAA' or s[i:i+3] == 'TGA' or s[i:i+3] == 'TAG':
                end_gene = i
                break
        return start_gene, end_gene + 3
    return None

def get_genes(s):
    genes = []
    i = 0
    while True:
        gene_holder = next_gene(i,s)
        print(gene_holder)
        if gene_holder == None:
            break
        genes.append(s[gene_holder[0]:gene_holder[1]])
        i = gene_holder[1]
    return genes

def gene_to_protein(gene):
    dna_dict = {'GCA':'A','GCC':'A','GCG':'A','GCT':'A','TGC':'C','TGT':'C','GAC':'D','GAT':'D','GAA':'E','GAG':'E','TTC':'F','TTT': 'F','GGA':'G','GGC':'G','GGG':'G','GGT':'G','CAC':'H','CAT':'H','ATA':'I','ATC':'I','ATT':'I','AAA':'K','AAG':'K','CTA':'L','CTC':'L','CTG':'L',"CTT":'L','TTA':'L','TTG':'L','ATG':'M','AAC':'N','ATT':'N','CCA':'P','CCC':'P','CCG':'P','CCT':'P','CAA':'Q','CAG':'Q','AGA':'R','AGG':'R','CGA':'R','CGC':'R','CGC':'R','CGG':'R','CGT':'R','AGC':'S','AGT':'S','TCA':'S','TCC':'S','TCG':'S','TCT':'S','ACA':'T','ACC':'T','ACG':'T','ACT':'T','GTA':'V','GTC':'T','GTG':'T','GTT':'T','TGG':'W','TAC':'Y','TAT':'Y','TAA':'','TAG':'','TGA':''}
    a_acid = ''
    dna_chunks = [gene[i:i+3] for i in range(0, len(gene),3)]
    for chunk in dna_chunks:
        a_acid += dna_dict[chunk] #Dictionary for random access with -> dict[key]
    return a_acid

def get_proteins(genes):
    r_genes= []
    for i in range(len(genes)):
        tmp = gene_to_protein(genes[i])
        if tmp != None:
            r_genes.append(tmp)
    return r_genes

def main():
    s = 'TCATTTGACTTAGCCATCATCATGGAACGTCGCTACTAATAAGTAACGTGTGCATTATGGCACGAAAAGAGACGTGAGAAAGTGCCTATGGAATCATACTTTGACCGAGCATGCCCCTCGAACTAATTGCTTTGGGCCCTTGGTTACGTATGCGAAAGAGACGATTGAAGTGGTAGCTTATAGGAAGAGATGCCGAGAGAGAGGGCTGAGCCTCAGTAACCCAGAATTATCACACGCGCTAATATGGAAAGCTCTATCATTTCCGCCGGTCGAGAGGCTACGCCATTGGCGTACGAACGATAA'
    # print(get_proteins(get_genes(s)))
    print(next_gene(39,s))
    while True:
        try:
            filename = input('Input the DNA file name (without suffix): ')
            f = open(filename + '.txt','r')
            data = f.read()
            f.close()
            break

        except:
            print('Please input a correct file name.')

            if filename == 'quit':
                sys.exit()

    wf = open(filename+'_proteins','w')
    proteins = get_proteins(get_genes(data))

    for i in range(len(proteins)):
        wf.write(proteins[i] + '\n')
    wf.close()
    print('Found', len(proteins), 'genes')

main()
protein_dict = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP',
}


def proteins(strand: str):
    protein_list = []

    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]

    for codon in codons:
        name = protein_dict.get(codon)
        if name == 'STOP':
            break
        protein_list.append(name)

    return protein_list

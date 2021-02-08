file1 = open("rosalind_dna.txt", 'r').read()
dict1 = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in range(len(file1)):
    if file1[i] == 'A':
        dict1['A'] += 1
    if file1[i] == 'C':
        dict1['C'] += 1
    if file1[i] == 'G':
        dict1['G'] += 1
    if file1[i] == 'T':
        dict1['T'] += 1

print(dict1['A'],  dict1['C'], dict1['G'], dict1['T'])

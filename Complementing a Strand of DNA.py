file1 = str(open("rosalind_revc.txt", 'r').read())
file2 = file1[::-1]
file3 = ''

for i in range(len(file1)):
    if file2[i] == 'A':
        file3 += "T"
    if file2[i] == 'C':
        file3 += "G"
    if file2[i] == 'G':
        file3 += "C"
    if file2[i] == 'T':
        file3 += "A"

print(file3)

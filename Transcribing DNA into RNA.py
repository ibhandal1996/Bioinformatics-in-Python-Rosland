file1 = str(open("rosalind_rna.txt", 'r').read())
file2 = ""
for i in range(len(file1)):
    if file1[i] == "T":
        file2 += "U"
    else:
        file2 += file1[i]

print(file2)
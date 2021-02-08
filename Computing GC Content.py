inp = open("rosalind_gc.txt", 'r').read().split(">")
inp.pop(0)

percentage = []

for i in range(0, len(inp)):
    countGC = 0
    countAT = 0
    for j in range(8, len(inp[i])):
        if inp[i][j] == "G" or inp[i][j] == "C":
            countGC += 1
        if inp[i][j] == "A" or inp[i][j] == "T":
            countAT += 1
    percentage.append(countGC/(countGC + countAT))

print(inp[percentage.index(max(percentage))][0:13])
print(max(percentage) * 100)

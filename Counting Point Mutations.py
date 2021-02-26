inp = open("rosalind_hamm.txt", 'r').read().split()

count = 0

for i in range(len(inp[1])):
    if inp[0][i] != inp[1][i]:
        count += 1

print(count)
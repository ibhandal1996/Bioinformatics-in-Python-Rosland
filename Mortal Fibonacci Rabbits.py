inp = (open("rosalind_fibd.txt", 'r').read().split())
for i in range(0, len(inp)):
    inp[i] = int(inp[i])

rabbits = [1, 1]

for i in range(2,inp[0]):
    if i < inp[1]:
        rabbits.append(rabbits[-2] + rabbits[-1])
    elif i == inp[1]:
        rabbits.append(rabbits[-2] + rabbits[-1] - 1)
    else:
        rabbits.append(rabbits[-2] + rabbits[-1] - rabbits[-(inp[1] + 1)])

print(rabbits[-1])

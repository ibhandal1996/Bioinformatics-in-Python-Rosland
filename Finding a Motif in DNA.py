inp = open("rosalind_subs.txt", 'r').read().split()

list1 = []

for i in range(0, len(inp[0])):
    if inp[1] == inp[0][i:i+len(inp[1])]:
        list1.append(i+1)

print(list1)
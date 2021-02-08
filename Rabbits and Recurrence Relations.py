inp = (open("rosalind_fib.txt", 'r').read().split())
for i in range(0, len(inp)):
    inp[i]= int(inp[i])

Adult_Rabbit_Pairs = 0
Baby_Rabbit_Pairs = 1

for i in range(1,inp[0]):
    All_Rabbit_Pairs = (Adult_Rabbit_Pairs * inp[1]) + Baby_Rabbit_Pairs
    Adult_Rabbit_Pairs = Baby_Rabbit_Pairs
    Baby_Rabbit_Pairs = All_Rabbit_Pairs

print(All_Rabbit_Pairs)

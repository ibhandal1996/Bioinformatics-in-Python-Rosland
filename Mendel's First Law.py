import itertools

inp = open("rosalind_iprb.txt", 'r').read().split()

pop = (['AA'] * int(inp[0])) + (['Aa'] * int(inp[1])) + (['aa'] * int(inp[2]))

count = 0
dom = 0

for i in pop:
    otherParents = pop[:]
    otherParents.remove(i)
    for j in otherParents:
        count += 4
        offspring = itertools.product(i, j)
        doms = filter(lambda k: 'A' in k, offspring)
        dom += len(list(doms))

print(dom/count)




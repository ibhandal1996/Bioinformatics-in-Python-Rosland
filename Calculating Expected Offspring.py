with open("rosalind_iev.txt") as file:
    inp = [int(x) for x in next(file).split()]

print((2*inp[0])+(2*inp[1])+(2*inp[2])+(2*inp[3]*.75)+(2*inp[4]*.5))

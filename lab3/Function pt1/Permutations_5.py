from itertools import permutations 
def perm(string):
    for i in permutations(string):
        print(''.join(i))

perm("ABC") #as example
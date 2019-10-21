from performance import Performance
from goody import irange
from graph_goody import random, spanning_tree

# Put script here to generate data for Problem #1
g = None

def create_random(n):
    global g
    g = random(n, lambda n : 10*n) 
    
for i in irange(0,7) :
    n = 1000 * 2**i
    p = Performance(lambda : spanning_tree(g), lambda : create_random(n),5,'Spanning Tree of size {}'.format(n))
    p.evaluate()
    p.analyze()
    print()

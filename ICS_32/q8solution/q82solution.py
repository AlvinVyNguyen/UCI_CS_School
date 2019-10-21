import cProfile
from graph_goody import random,spanning_tree
import pstats

# Put script here to generate data for Problem #2

g = random (50000, lambda n : 10*n)
cProfile.run('spanning_tree(g)','profile50K')
p = pstats.Stats('profile50K')
p.strip_dirs().sort_stats('ncalls').print_stats()

g = random (100000, lambda n : 10*n)
cProfile.run('spanning_tree(g)','profile100K')
p = pstats.Stats('profile100K')
p.strip_dirs().sort_stats('time').print_stats()


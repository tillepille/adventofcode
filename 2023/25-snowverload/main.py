import sys
import networkx as nx

g = nx.Graph()

file = open(sys.argv[1]).read().strip()

for line in file.split("\n"):
    p = line.split()
    for t in p[1:]:
        g.add_edge(p[0][:-1], t)
cv, p = nx.stoer_wagner(g)

print(len(p[0]) * len(p[1]))

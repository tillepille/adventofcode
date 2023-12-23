import sys
sys.setrecursionlimit(10000)
file = open(sys.argv[1]).read().strip()

graph = {}

map = [list(line) for line in file.split("\n")]

start = (0, map[0].index('.'))
end = (len(map)-1, map[len(map)-1].index('.'))

for i,line in enumerate(map):
  for v,c in enumerate(line):
    graph[(i,v)] = []
    for x,y in [[-1,0],[0,1],[1,0],[0,-1]]:
      if i+x < 0 or i+x >= len(map) or v+y < 0 or v+y >= len(map[0]):
        continue
      if c == '#': continue
      if map[i+x][v+y] == '.':
        graph[(i,v)].append((i+x,v+y))
      if x == 0 and y == 1 and map[i+x][v+y] == '>':
        graph[(i,v)].append((i+x,v+y))
      if x == 1 and y == 0 and map[i+x][v+y] == 'v':
        graph[(i,v)].append((i+x,v+y))

# filter out empty edges
graph = {k: v for k, v in graph.items() if len(v) > 0}

def dfs_paths(s, e, path=[]):
    path = path + [s]
    if s == e:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[s]:
        if node not in path:
          new_paths = dfs_paths(node, end, path)
          paths.extend(new_paths)
    return paths

paths = dfs_paths(start, end)
pathlens = [len(path)-1 for path in paths]
print(max(pathlens))

import sys
file = open(sys.argv[1]).read().strip()

map = file.split("\n")
map = [list(x) for x in map]

path = []
start = (0,0,64)
tiles = set()
visited = set()

for i,line in enumerate(map):
  for v,c in enumerate(line):
    if c == 'S':
      start = (i,v,64)
      path.append(start)
      break

while path:
  i,v,stepsLeft = path.pop(0)
  if i < 0 or i >= len(map) or v < 0 or v >= len(map[0]) or map[i][v] == '#':
    continue
  if (i,v) in visited:
    continue
  visited.add((i,v))
  if stepsLeft >= 0 and stepsLeft % 2 == 0:
    tiles.add((i,v))
  for x,y in [[-1,0],[0,1],[1,0],[0,-1]]:
    path.append((i+x,v+y,stepsLeft-1))

print(len(tiles))

import sys,time
file = open(sys.argv[1]).read().strip()

map = file.split("\n")
map = [list(x) for x in map]



for i,line in enumerate(map):
  for v,c in enumerate(line):
    if c == 'S':
      start = (i,v,64)
      break

def getEndlessElem(i,v):
  x = i % len(map)
  y = v % len(map[0])
  return map[x][y]

multis = [len(map)/2, len(map)/2 + len(map),len(map)/2 + len(map)*2]
results = []
for m in multis:
  path = []
  path.append((start[0],start[1],m))
  tiles = set()
  visited = set()
  while path:
    i,v,stepsLeft = path.pop(0)
    if getEndlessElem(i,v) == '#':
      continue
    if (i,v) in visited:
      continue
    visited.add((i,v))
    if stepsLeft >= 0 and stepsLeft % 2 == 0:
      tiles.add((i,v))
    if stepsLeft == 0:
      continue
    for x,y in [[-1,0],[0,1],[1,0],[0,-1]]:
      path.append((i+x,v+y,stepsLeft-1))
  results.append(len(tiles))

f = 26501365 / 131
c = results[0]
a = (results[2] + c - 2 * results[1]) / 2
b = results[1] - c -a

print(a*(f*f) + b*f + c)

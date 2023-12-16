import sys
sys.setrecursionlimit(10000)
file = open(sys.argv[1]).read().strip()

map = file.split("\n")
map = [list(x) for x in map]

def getValue(a,b):
  return map[a][b]

def getNext(a,b,d):
  x = a
  y = b
  if d == 0:
    x =  a - 1
  if d == 1:
    y = b + 1
  if d == 2:
    x =  a + 1
  if d == 3:
    y = b - 1
  return x,y

def m(a,b,d):
  if a < 0 or b < 0 or a >= len(map) or b >=len(map[0]):
    return
  if (a,b,d) in visits:
    return
  visits.append((a,b,d))
  if getValue(a,b) == '.' or (getValue(a,b) == '|' and (d == 0 or d == 2)) or (getValue(a,b) == '-' and (d == 1 or d == 3)):
    x,y = getNext(a,b,d)
    m(x,y,d)
    return
  if getValue(a,b) == '|' and (d == 1 or d == 3):
    m(a-1,b,0)
    m(a+1,b,2)
  if getValue(a,b) == '-' and (d == 0 or d == 2):
    m(a,b-1,3)
    m(a,b+1,1)
  if getValue(a,b) == '\\':
    if d == 0:
      m(a,b-1,3)
    if d == 1:
      m(a+1,b,2)
    if d == 2:
      m(a,b+1,1)
    if d == 3:
      m(a-1,b,0)
  if getValue(a,b) == '/':
    if d == 0:
      m(a,b+1,1)
    if d == 1:
      m(a-1,b,0)
    if d == 2:
      m(a,b-1,3)
    if d == 3:
      m(a+1,b,2)

edges = []
for i in range(len(map)):
  edges.append((i,0,1))
  edges.append((i,len(map[0])-1,3))

for i in range(len(map[0])):
  edges.append((0,i,2))
  edges.append((len(map)-1,i,0))

results = []
for edge in edges:
  visits = []
  a,b,d = edge[0],edge[1],edge[2]
  m(a,b,d)
  activeTiles = set()
  for visit in visits:
    activeTiles.add((visit[0],visit[1]))
  results.append(len(activeTiles))

print(max(results))

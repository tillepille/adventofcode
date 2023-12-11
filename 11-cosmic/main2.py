import sys

file = open(sys.argv[1]).read().strip()

map = file.split('\n')
map = [list(x) for x in map]

emptyLines = []
i = 0
while i < len(map): 
  if not '#' in map[i]:
    emptyLines.append(i)
  i += 1

emptyRows = []
v = 0
while v < len(map[0]):
  emptyRow = True
  for line in map:
    if line[v] == '#':
      emptyRow = False
  if emptyRow:
    emptyRows.append(v)
  v += 1

galaxies = []

for i, line in enumerate(map):
  for v, item in enumerate(line):
    if item == '#':
      galaxies.append((i,v))

def getDistance(a, b):
  pureDistance = abs(a[0] - b[0]) + abs(a[1] - b[1])
  # print(a,b)
  # print(pureDistance)
  for el in emptyLines:
    if  a[0] < el < b[0] or b[0] < el < a[0]:
      pureDistance += 1000000-1
  for er in emptyRows:
    if a[1] < er < b[1] or b[1] < er < a[1]:
      pureDistance += 1000000-1
  # print(pureDistance)
  # print()
  return pureDistance

result = 0
for i, g in enumerate(galaxies):
  for v in range(i+1, len(galaxies)):
    dist = getDistance(galaxies[i], galaxies[v])
    result += dist

print(result)

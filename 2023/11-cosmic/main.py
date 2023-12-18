import sys

file = open(sys.argv[1]).read().strip()

map = file.split('\n')
map = [list(x) for x in map]

i = 0
while i < len(map): 
  if not '#' in map[i]:
    map.insert(i, map[i])
    i += 2
  else:
    i += 1

v = 0
while v < len(map[0]):
  emptyRow = True
  for line in map:
    if line[v] == '#':
      emptyRow = False
  print('row is empty', v)
  if emptyRow:
    i2 = 0
    while i2 < len(map):
      map[i2].insert(v, '.')
      i2 += 1
    v += 2
  else:
    v += 1

galaxies = []

for i, line in enumerate(map):
  for v, item in enumerate(line):
    if item == '#':
      galaxies.append((i,v))

def getDistance(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

result = 0
for i, g in enumerate(galaxies):
  for v in range(i, len(galaxies)):
    result += getDistance(galaxies[i], galaxies[v])

print(result)
import sys

file = open(sys.argv[1]).read().strip()

map = file.split("\n")
map = [list(x) for x in map]

def rollNorth(i,v):
  if map[i-1][v] == '.' and i > 0:
    map[i-1][v] = 'O'
    map[i][v] = '.'
    rollNorth(i-1,v)

def rollWest(i,v):
  if map[i][v-1] == '.' and v > 0:
    map[i][v-1] = 'O'
    map[i][v] = '.'
    rollWest(i,v-1)

def rollSouth(i,v):
  if i < len(map)-1 and map[i+1][v] == '.':
    map[i+1][v] = 'O'
    map[i][v] = '.'
    rollSouth(i+1,v)

def rollEast(i,v):
  if v < len(map[i])-1 and map[i][v+1] == '.':
    map[i][v+1] = 'O'
    map[i][v] = '.'
    rollEast(i,v+1)

weights = []

for x in range(1000): # should 1000000000
  # north
  for i in range(1,len(map)):
    for v in range(len(map[i])):
      if map[i][v] == 'O':
        rollNorth(i,v)
  # west
  for v in range(len(map[0])):
    for i in range(0,len(map)):
      if map[i][v] == 'O':
        rollWest(i,v)
  #south
  for i in reversed(range(0, len(map))):
    for v in range(len(map[i])):
      if map[i][v] == 'O':
        rollSouth(i,v)
  # east
  for v in reversed(range(0,len(map[0]))):
    for i in range(len(map)):
      if map[i][v] == 'O':
        rollEast(i,v)
  result = 0
  weight = len(map)
  for line in map:
    for tile in line:
      if tile == 'O':
        result += weight
    weight = weight - 1
  weights.append(result)

print(weights)

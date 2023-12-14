import sys

file = open(sys.argv[1]).read().strip()

map = file.split("\n")
map = [list(x) for x in map]

def roll(i,v):
  if map[i-1][v] == '.' and i > 0:
    map[i-1][v] = 'O'
    map[i][v] = '.'
    roll(i-1,v)

for i in range(1,len(map)):
  for v in range(len(map[i])):
    if map[i][v] == 'O':
      roll(i,v)

result = 0
weight = len(map)

for line in map:
  for tile in line:
    if tile == 'O':
      result += weight
  weight = weight - 1

print(result)
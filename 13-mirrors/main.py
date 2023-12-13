import sys

file = open(sys.argv[1]).read().strip()

blocks = file.split("\n\n")
hMirrors = []
vMirrors = []

def isMirror(i,v, lines):
  if lines[v] == lines[i]:
    if v == len(lines)-1 or i == 0:
      return True
    else:
      return isMirror(i-1, v+1, lines)
  else:
    return False

for block in blocks:
  lines = block.split('\n')
  lines = [list(x) for x in lines]
  rows = [[row[i] for row in lines] for i in range(len(lines[0]))]
  for i in range(1,len(lines)):
    if isMirror(i-1, i, lines):
      hMirrors.append(i * 100)
  for i in range(1, len(rows)):
    if isMirror(i-1, i, rows):
      vMirrors.append(i)

print(sum(hMirrors) + sum(vMirrors))

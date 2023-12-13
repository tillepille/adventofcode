import sys

file = open(sys.argv[1]).read().strip()

blocks = file.split("\n\n")
hMirrors = []
vMirrors = []

def isMirror(i,v, lines, smudges):
  smudges += sum(lines[i][x] != lines[v][x] for x in range(len(lines[i])) )
  if smudges < 2:
    if v == len(lines)-1 or i == 0:
      return smudges == 1
    else:
      return isMirror(i-1, v+1, lines,smudges)
  else:
    return False

for block in blocks:
  lines = block.split('\n')
  lines = [list(x) for x in lines]
  rows = [[row[i] for row in lines] for i in range(len(lines[0]))]
  smudges = 0
  for i in range(1,len(lines)):
    if isMirror(i-1, i, lines, smudges):
      hMirrors.append(i * 100)
  for i in range(1, len(rows)):
    if isMirror(i-1, i, rows, smudges):
      vMirrors.append(i)

print(sum(hMirrors) + sum(vMirrors))

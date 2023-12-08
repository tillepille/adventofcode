import sys, re

file = open(sys.argv[1]).read().strip()

lines = file.split('\n')

directions = list(lines.pop(0))
next = 'AAA'
end = 'ZZZ'
hops = 0
lines.pop(0) # remove empty line

nodeGraph = {}

for line in lines:
  res = re.search("(\w+) = \((\w+), (\w+)\)",line)
  p1 = res.group(1)
  p2 = res.group(2)
  p3 = res.group(3)
  nodeGraph[p1] = (p2, p3)

def getDirection ():
  nextDir = directions[hops % len(directions)]
  if nextDir == 'R':
    return 1
  else:
    return 0

while next != end:
  next = nodeGraph[next][getDirection()]
  hops +=1

print(hops)
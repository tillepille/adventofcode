import sys, re, math, functools

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

starts = list({k: v for k, v in nodeGraph.items() if k.endswith('A')}.keys())
print('starts', starts)


ends = []
for i, next in enumerate(starts):
  hops = 0
  directionCycles = 0
  while True:
    next = nodeGraph[next][getDirection()]
    if next.endswith('Z'):
      ends.append(hops + 1)
      print(next, hops)
      break
    hops += 1
print(ends)
print(math.lcm(*ends))

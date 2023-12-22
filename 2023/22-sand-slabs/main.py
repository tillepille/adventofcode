import sys
file = open(sys.argv[1]).read().strip()

bricks = []

for brick in file.split("\n"):
  s, e = (brick.split("~"))
  s = [int(x) for x in s.split(",")]
  e = [int(x) for x in e.split(",")]
  bricks.append((s,e))

bricks.sort(key = lambda x: x[0][2])

hasSupport = {i:[] for i in range(len(bricks))}
givesSupport = {i:[] for i in range(len(bricks))}

def moveBrickDown(i, h):
  bricks[i][0][2] = bricks[i][0][2] - h
  bricks[i][1][2] = bricks[i][1][2] - h

def getPoints(b):
  points = []
  for x in range(b[0][0], b[1][0]+1):
    for y in range(b[0][1], b[1][1]+1):
      points.append((x, y))
  return points

def touching(i):
  if bricks[i][0][2] == 1:
    return
  else:
    for v in reversed(range(i)):
      if bricks[v][1][2] == bricks[i][0][2] - 1:
        for p in getPoints(bricks[i]):
          if p in getPoints(bricks[v]):
            givesSupport[v].append(i)
            hasSupport[i].append(v)
            break
  return len(hasSupport[i])

for i in range(len(bricks)):
  while 1 > touching(i):
    moveBrickDown(i, 1)

bricks.sort(key = lambda x: x[0][2])
hasSupport = {i:[] for i in range(len(bricks))}
givesSupport = {i:[] for i in range(len(bricks))}

for i in range(len(bricks)):
  touching(i)


total = 0
for i in range(len(bricks)):
  if all(len(hasSupport[j]) >= 2 for j in givesSupport[i]):
    total += 1
print(total)
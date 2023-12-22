import sys, time
file = open(sys.argv[1]).read().strip()

bricks = []
hasSupport = {}
getName= list('ABCDEFG')
for brick in file.split("\n"):
  s, e = (brick.split("~"))
  s = [int(x) for x in s.split(",")]
  e = [int(x) for x in e.split(",")]
  bricks.append((s,e))

bricks.sort(key = lambda x: x[0][2])

def moveBrickDown(i, h):
  bricks[i][0][2] = bricks[i][0][2] - h
  bricks[i][1][2] = bricks[i][1][2] - h

def lineIntersection(b1, b2):
  # https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines-in-python
  line1 = ((b1[0][0], b1[0][1]), (b1[1][0], b1[1][1]))
  line2 = ((b2[0][0], b2[0][1]), (b2[1][0], b2[1][1]))
  # hack for points
  if line1[0] == line1[1]:
    line1 = (line1[0], (line1[1][0], line1[1][1] + 1))
  if line2[0] == line2[1]:
    line2 = (line2[0], (line2[1][0], line2[1][1] + 1))

  xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
  ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

  def det(a, b):
    return a[0] * b[1] - a[1] * b[0]

  div = det(xdiff, ydiff)
  if div == 0:
    return False
  return True

def touching(i):
  touches = []
  if bricks[i][0][2] == 1:
    print(i,'is grounded', bricks[i])
    touches.append(-1)
  else:
    for v in reversed(range(i)):
      if bricks[v][1][2] == bricks[i][0][2] - 1: # is on next layer
        if lineIntersection(bricks[i], bricks[v]):
          touches.append(v)
  hasSupport[i] = touches
  return len(touches)

for i in range(len(bricks)):
  while 1 > touching(i):
    moveBrickDown(i, 1)

canBeRemoved = set()
for b in hasSupport.keys():
  if len(hasSupport[b]) > 1:
    for s in hasSupport[b]:
      canBeRemoved.add(s)
print(len(canBeRemoved)+1)

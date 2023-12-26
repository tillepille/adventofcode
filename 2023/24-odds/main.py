import sys

file = open(sys.argv[1]).read().strip()
# file = open('/Users/tls/dev/github.com/tillepille/adventofcode/2023/24-odds/input-test.txt').read().strip()

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
      return 0,0 # do not cross

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def collisionInPast(hs, x,y):
  collision = True
  if hs[1][0] < 0:
    if x <= hs[0][0]:
      collision = False
  else:
    if x >= hs[0][0]:
      collision = False
  if hs[1][1] < 0:
    if y <= hs[0][1]:
      collision = False
  else:
    if y >= hs[0][1]:
      collision = False
  return collision


hs = []
collisions = []
pastCollisions = []
testMin = 200000000000000
testMax = 400000000000000

for line in  file.split("\n"):
  pos, dir = line.split("@")
  pos = tuple([int(x.strip()) for x in pos.split(",")][:2])
  dir = tuple([int(x.strip()) for x in dir.split(",")][:2])
  hs.append((pos,dir))

for i in range(len(hs)):
  A = hs[i][0]
  B = (A[0]+hs[i][1][0], A[1]+hs[i][1][1])
  for j in range(i+1, len(hs)):
    C = hs[j][0]
    D = (C[0]+hs[j][1][0], C[1]+hs[j][1][1])
    x,y = line_intersection((A,B), (C,D))
    if testMin <= x <= testMax and testMin <= y <= testMax:
      collisions.append((i, j, x, y))

for col in collisions:
  hs1 = hs[col[0]]
  hs2 = hs[col[1]]
  x,y = col[2], col[3]
  if collisionInPast(hs1, x,y) or collisionInPast(hs2, x,y):
    pastCollisions.append(col)

collisions = [x for x in collisions if x not in pastCollisions]

print(len(collisions))

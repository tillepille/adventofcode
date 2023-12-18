import sys
file = open(sys.argv[1]).read().strip()

lines = file.split("\n")
start = (0,0)
trenches = []
trenches.append(start)

trenchLength = 0

for line in lines:
  line = line.split()
  dir = line[0]
  l = int(line[1])
  trenchLength += l
  color = line[2]
  lastElem = trenches[-1]
  if dir == 'R':
    trenches.append((lastElem[0], lastElem[1] + l))
  if dir == 'L':
    trenches.append((lastElem[0], lastElem[1] - l))
  if dir == 'D':
    trenches.append((lastElem[0] + l, lastElem[1]))
  if dir == 'U':
    trenches.append((lastElem[0] - l, lastElem[1]))

def area(corners):
    n = len(corners)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

innerPoints = area(trenches) - (trenchLength // 2) + 1 

print(int(innerPoints + trenchLength))

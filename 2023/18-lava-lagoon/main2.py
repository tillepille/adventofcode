import sys,re
file = open(sys.argv[1]).read().strip()

lines = file.split("\n")
start = (0,0)
trenches = []
trenches.append(start)

trenchLength = 0

for line in lines:
  hexCode = re.search('#(\w+)',line).group(1)
  dir = int(hexCode[-1:])
  l = int(hexCode[:5],16)
  trenchLength += l
  lastElem = trenches[-1]
  if dir == 0:
    trenches.append((lastElem[0], lastElem[1] + l))
  if dir == 2:
    trenches.append((lastElem[0], lastElem[1] - l))
  if dir == 1:
    trenches.append((lastElem[0] + l, lastElem[1]))
  if dir == 3:
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

import sys, re
from collections import defaultdict
file = open(sys.argv[1]).read().strip()

m = []
gears = set()
ratios = defaultdict(list)
for i,line in enumerate(file.split('\n')):
  m.append(list(line))

def isMatch(string):
  if len(re.findall("[^\d|\.]", string)) > 0:
    return True

def hasAdjacent(x,y):
  adj = False
  for a in [x-1, x, x+1]:
    if a >= 0 and a < len(m)-1 and isMatch(m[a][y]):
      adj = True
      if m[a][y] == "*":
        number, nextIndex = getFullNumber(x,y)
        ratios[(a,y)].append(number)
      break
    for b in [y-1, y, y+1]:
      if a >= 0 and a < len(m)-1 and b >= 0 and b < len(m[a])-1 and isMatch(m[a][b]):
        adj = True
        if m[a][b] == "*":
          number, nextIndex = getFullNumber(x,y)
          ratios[(a,b)].append(number)
        break
  return adj

def getFullNumber(x,y):
    forward= y
    backward = y
    while forward < len(m[x])-1 and m[x][forward+1].isdigit():
      forward += 1
    while backward >= 0 and m[x][backward-1].isdigit():
      backward -= 1
    numberList = []
    for yy in range(backward, forward +1):
      numberList.append(m[x][yy])
    number=int(''.join(numberList))
    return number,forward


result1 = 0
result2 = 0

for x in range(len(m)):
  y = 0
  while y < len(m[x]):
    if len(re.findall("\d",m[x][y])) > 0:
      if hasAdjacent(x,y):
        number, nextIndex = getFullNumber(x,y)
        result1 += number
        y = nextIndex + 1
      else:
        y += 1
    else:
      y += 1

for gear,numbers in ratios.items():
  if len(numbers)==2:
    result2 += numbers[0]*numbers[1]

print("result 1:",result1)
print("result 2:",result2)

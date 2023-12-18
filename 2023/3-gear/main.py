import sys, re

file = open(sys.argv[1]).read().strip()

m = []
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
      break
    for b in [y-1, y, y+1]:
      if a >= 0 and a < len(m)-1 and b >= 0 and b < len(m[a])-1 and isMatch(m[a][b]):
        adj = True
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
      print(m[x][yy])
      numberList.append(m[x][yy])
    number=int(''.join(numberList))
    return number,forward


result = 0

for x in range(len(m)):
  y = 0
  while y < len(m[x]):
    if len(re.findall("\d",m[x][y])) > 0:
      if hasAdjacent(x,y):
        number, nextIndex = getFullNumber(x,y)
        result += number
        y = nextIndex + 1
      else:
        y += 1
    else:
      y += 1

print(result)

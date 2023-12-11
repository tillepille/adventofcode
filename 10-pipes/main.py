import sys

file = open(sys.argv[1]).read().strip()

lines = file.split('\n')

start = ()

for i,line in enumerate(lines):
  iofS = line.find('S')
  if iofS != -1:
    start = (i, iofS)
    break

map = [list(x) for x in lines]
next = start
dir = 1 # 0 n 1 e 2 s 3 w
path = []

count = 0

def add(x):
  path.append(get(x))

def get(x):
  return map[x[0]][x[1]]

if map[start[0]][start[1]+1] == '-' or map[start[0]][start[1]+1] == 'J' or map[start[0]][start[1]+1] == '7':
  next = (start[0],start[1]+1)
  dir = 1
elif map[start[0]][start[1]-1] == '-' or map[start[0]][start[1]-1] == 'L' or map[start[0]][start[1]-1] == 'F':
  next = (start[0],start[1]-1)
  dir = 3
elif map[start[0]+1][start[1]] == '|' or map[start[0]+1][start[1]]  == 'J' or map[start[0]+1][start[1]] == 'L':
  next = (start[0]+1,start[1])
  dir = 2
elif map[start[0]-1][start[1]] == '|' or map[start[0]-1][start[1]] == 'F' or map[start[0]-1][start[1]] == '7':
  next = (start[0]-1,start[1])
  dir = 0
add(next)

while get(next) != 'S':
# L is a 90-degree bend connecting north and east.
  if get(next) == 'L':
    if dir == 3:
      next = (next[0]-1,next[1])
      dir = 0
    elif dir == 2:
      next = (next[0],next[1]+1)
      dir = 1
    else:
      break
# J is a 90-degree bend connecting north and west.
  elif get(next) == 'J':
    if dir == 2:
      next = (next[0],next[1]-1)
      dir = 3
    elif dir == 1:
      next = (next[0]-1,next[1])
      dir = 0
    else:
      break
# 7 is a 90-degree bend connecting south and west.
  elif get(next) == '7':
    if dir == 1:
      next = (next[0]+1,next[1])
      dir = 2
    elif dir == 0:
      next = (next[0],next[1]-1)
      dir = 3
    else:
      break
# F is a 90-degree bend connecting south and east.
  elif get(next) == 'F':
    if dir == 0:
      next = (next[0],next[1]+1)
      dir = 1
    elif dir == 3:
      next = (next[0]+1,next[1])
      dir = 2
    else:
      break
# | is a vertical pipe connecting north and south.
  elif get(next) == '|':
    if dir == 2:
      next = (next[0]+1,next[1])
    else:
      next = (next[0]-1,next[1])
# - is a horizontal pipe connecting east and west.
  elif get(next) == '-':
    if dir == 3:
      next = (next[0],next[1]-1)
    else:
      next = (next[0],next[1]+1)
  elif get(next) == '.':
    break
  # time.sleep(1)
  add(next)
print(int(len(path)/2))

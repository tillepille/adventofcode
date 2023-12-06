import sys, re

file = open(sys.argv[1]).read().strip()

lines = file.split('\n')

times = lines.pop(0).split(":")[1].split()
dists = lines.pop(0).split(":")[1].split()

result = 1
for i, time in enumerate(times):
  dist = int(dists[i])
  time = int(time)
  wins = 0
  for v in range(time):
    buttonTime = time - v
    if v * buttonTime > dist:
      wins += 1
  result = result * wins

print(result)
  
import sys, re

file = open(sys.argv[1]).read().strip()

lines = file.split('\n')

times = lines.pop(0).split(":")[1].split()
dists = lines.pop(0).split(":")[1].split()

finalTime = int(''.join(times))
finalDist = int(''.join(dists))

wins = []
dist = finalDist
time = finalTime
wins.append(0)
for v in range(time):
  buttonTime = time - v
  if v * buttonTime > dist:
    wins[0] += 1

print(wins)
result = 1
for win in wins:
  result = result * win
print(result)

  
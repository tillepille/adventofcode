import sys, re

file = open(sys.argv[1]).read().strip()

result = 0

for i,line in enumerate(file.split('\n')):
  line = line.split(":")[1]
  wins = line.split("|")[0].split()
  cards = line.split("|")[1].split()
  lineResult = 0
  for win in wins:
    if win in cards:
      if lineResult == 0:
        lineResult += 1
      else:
        lineResult = lineResult *2
  result += lineResult
print(result)

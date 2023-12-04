import sys, re

file = open(sys.argv[1]).read().strip()

result = 0
winningCards = []
for i,line in enumerate(file.split('\n')):
  line = line.split(":")[1]
  wins = line.split("|")[0].split()
  cards = line.split("|")[1].split()
  lineResult = 0
  copies = winningCards.count(i) + 1
  winningCards.append(i)
  for win in wins:
    if win in cards:
      lineResult += 1
  if lineResult > 0:
    for result in range(i + 1, i + lineResult + 1):
      for copy in range(copies):
        winningCards.append(result)

print(len(winningCards))

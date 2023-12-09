import sys

file = open(sys.argv[1]).read().strip()

lines = file.split('\n')

def getDiffs (list):
  diffs = []
  i = 0
  while i < len(list) -1:
    diffs.append(list[i+1] - list[i])
    i += 1 
  return diffs

predictions = []

for line in lines:
  line = [int(x) for x in line.split()]
  forecast = [line]
  while not all(x == 0 for x in line):
    diffs = getDiffs(line)
    forecast.append(diffs)
    line = diffs
  i = len(forecast) - 1
  forecast[-1].append(0)
  while i > 0:
    forecast[i-1].append(forecast[i][-1] + forecast[i-1][-1])
    # recursive? get elements, add to parent i-1 list
    i = i - 1
  predictions.append(forecast[0][-1])

print(sum(predictions))

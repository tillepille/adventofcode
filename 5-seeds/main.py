import sys, re

file = open(sys.argv[1]).read().strip()

lines = file.split('\n')

seeds = lines.pop(0).split(":")[1].split()
  
locations = []
print(seeds)
for seed in seeds:
  seed = int(seed)
  converted = False
  for line in lines:
    if line == "":
      converted = False
    if not ":" in line and line != "" and not converted:
      numbers = line.split()
      start = int(numbers[1])
      offset = int(numbers[0]) - int(numbers[1])
      max = int(numbers[2])
      if seed in range(start, start + max):
        seed = seed + offset
        converted = True
  locations.append(seed)

print(locations)
print(min(locations))
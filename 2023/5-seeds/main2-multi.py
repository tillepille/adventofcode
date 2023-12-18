import sys
from multiprocessing import Process

file = open(sys.argv[1]).read().strip()

lines = file.split('\n')
minLocation = 487758422
threads = list()
seeds = lines.pop(0).split(":")[1].split()


def findMinLocation (one, two):
  minLocation = one + two
  for seed in range(one, one + two):
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
    if seed <= minLocation:
      minLocation = seed
  print('finished', one, two, 'result' , minLocation)

if __name__ == '__main__':
  while len(seeds) > 1:
    one = int(seeds.pop(0))
    two = int(seeds.pop(0))
    x = Process(target=findMinLocation, args=(one,two))
    threads.append(x)
    x.start()

  for index, thread in enumerate(threads):
    thread.join()
    print("Main    : thread done", index)

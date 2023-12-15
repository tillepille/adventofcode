import sys

file = open(sys.argv[1]).read().strip()

def calc(seq):
  r = 0
  for c in seq:
    r = (r + ord(c)) * 17 % 256
  return r

seqs = file.split(',')
results = []
for seq in seqs:
  results.append(calc(seq))

print(sum(results))

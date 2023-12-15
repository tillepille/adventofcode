import sys,re,time

file = open(sys.argv[1]).read().strip()

def calc(seq):
  r = 0
  for c in seq:
    r = (r + ord(c)) * 17 % 256
  return r

seqs = file.split(',')
boxes = [[] * 1 for i in range(256)]
for seq in seqs:
  label = re.search('[a-z]+',seq)[0]
  boxNo = calc(label)
  if '=' in seq:
    lensNo = int(list(seq)[-1])
    newLense = (label,lensNo)
    s = True
    for i,lense in enumerate(boxes[boxNo]):
      if lense[0] == label:
        boxes[boxNo][i] = newLense
        s = False
    if s:
      boxes[boxNo].append(newLense)
  if '-' in seq:
    boxes[boxNo] =[x for x in boxes[boxNo] if x[0]!=label]

result = 0
for i, box in enumerate(boxes):
  for v, lense in enumerate(box):
    result += ( i + 1 ) * ( v + 1 ) * lense[1]
print(result)
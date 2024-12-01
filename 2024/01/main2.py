import sys

file = open(sys.argv[1]).read().strip()

result = 0

left = []
right =  []
for i,line in enumerate(file.split('\n')):
  left.append(int(line.split('   ')[0]))
  right.append(int(line.split('   ')[1]))

result = 0
for i, item in enumerate(left):
  similarity = right.count(item) * item
  print(similarity)
  result += similarity

print(result)

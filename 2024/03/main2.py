import sys, re

file = open(sys.argv[1]).read().strip()
file = file.replace('\n','')
result = 0

line = re.sub(r"don't\(\)(.*?)do\(\)", '', file)
numbers = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
for tuple in numbers:
  num1 = int(tuple[0])
  num2 = int(tuple[1])
  result += num1 * num2

print(result)

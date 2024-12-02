import sys

file = open(sys.argv[1]).read().strip()

result = 0

for i,line in enumerate(file.split('\n')):

  report = line.split(' ') 
  report = [int(x) for x in report]
  ordered = False
  shallow = True
  if report == sorted(report) or report == sorted(report, reverse=True):
    ordered = True
  
  for i in range(len(report)-1):
    diff = abs(int(report[i+1]) - int(report[i]))
    if  diff == 0 or diff > 3:
      shallow = False

  if ordered and shallow:
    result += 1
print(result)

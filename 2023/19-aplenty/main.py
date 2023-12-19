import sys,re,ast
file = open(sys.argv[1]).read().strip()
workflows = file.split("\n\n")[0].split("\n")
ratings = file.split("\n\n")[1].split("\n")

def quote(match_obj):
  if match_obj.group() is not None:
    return '"'+match_obj.group(1)+'"'

for line in workflows:
  r = re.search('(\w+){(.+)}', line)
  name = r.group(1)
  rule = r.group(2)
  rule = rule.replace('A','"A"')
  rule = rule.replace('R','"R"')
  rule = re.sub('(([a-z][a-z]+))', quote,rule)
  rule = rule.replace(',',' or ')
  rule = rule.replace(':',' and ')
  rule = ''.join((name,'_ = lambda: ', rule))
  exec(rule)

sum = 0
for part in ratings:
  p = part.replace(',',';')
  fu = 'in_()'
  res = ''
  while True:
    exec(p[1:-1] + ';res='+fu)
    if res == 'R':
      break
    if res == 'A':
      sum += x+m+a+s
      break
    fu = res + '_()'

print(sum)
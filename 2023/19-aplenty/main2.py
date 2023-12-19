import sys,re
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

splits = {c: [0, 4000] for c in 'xmas'}

for line in workflows:
  for c,o,v in re.findall(r'(\w+)(<|>)(\d+)', line):
    splits[c].append(int(v)-(o=='<'))

ranges = lambda x: [(a,a-b) for a,b in zip(x[1:], x)]
X,M,A,S = [ranges(sorted(splits[x])) for x in splits]

sum2 = 0
for x,dx in X:
  for m,dm in M:
    for a,da in A:
      for s,ds in S:
        fu = 'in_()'
        res = ''
        while True:
          exec('res='+fu)
          if res == 'R':
            break
          if res == 'A':
            comb = dx * dm * da * ds 
            sum2 += comb
            break
          fu = res + '_()'
print(sum2)

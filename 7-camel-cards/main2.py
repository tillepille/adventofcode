import sys, re

file = open(sys.argv[1]).read().strip()

lines = file.split('\n')

lines = [ line.split() for line in lines ]
finals = []
cards = {
  'A': 13, 
  'K': 12, 
  'Q': 11, 
  'J': 0, 
  'T': 9, 
  '9': 8, 
  '8': 7, 
  '7': 6, 
  '6': 5, 
  '5': 4, 
  '4': 3, 
  '3': 2,
  '2': 1
  }

def getScore(str):
  score = 0
  jokers = str.count('J')
  sstr = str.replace('J','')
  if jokers == 5: 
    sstr = str
  kinds = {i:sstr.count(i) for i in sstr}
  kindList = list(kinds.values())
  kindList.sort(reverse=True)
  if jokers > 0:
    print('hasJokers', jokers)
    kindList[0] = kindList[0] + jokers
  if kindList[0] >= 5:
    score = 600000000000
  elif kindList[0] == 4:
    score = 500000000000
  elif kindList[0] == 3 and kindList[1] == 2: #fullhouse
    score = 400000000000
  elif kindList[0] == 3: # three pair
    score = 300000000000
  elif kindList[0] == 2 and kindList[1] == 2: #two pair
    score = 200000000000
  elif kindList[0] == 2: # one pair
    score = 100000000000
  highCard= 0
  for c in str:
    highCard = highCard*100+ cards.get(c)
  score = score + highCard
  print(str, sstr, kindList ,score)
  return score

for line in lines:
  hand = line[0]
  bid = int(line[1])
  score = getScore(hand)
  finals.append((score, bid))

finals.sort(key=lambda a: a[0])
total = 0
for i, final in enumerate(finals):
  fscore = (i + 1)  * final[1]
  total = total + fscore
  # print(i, final)
print(total)

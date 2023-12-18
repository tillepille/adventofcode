import re
f = open("input.txt", "r")
games = f.readlines()

gameId = 1
result = 0
for game in games:
  game = re.sub("Game \d+\:","", game)
  gameWorks = True
  plays = game.split(";")
  for play in plays:
    cubeSets = play.split(",")
    for cubeSet in cubeSets:
      cubes = cubeSet.split()
      count = int(cubes[0])
      color = cubes[1]
      if (color == "red" and count > 12) or (color == "blue" and count > 14) or (color == "green" and count > 13):
        gameWorks = False
  if gameWorks:
    result += gameId
  gameId += 1

print(result)

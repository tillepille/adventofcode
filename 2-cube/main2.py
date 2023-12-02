import re
f = open("input-test.txt", "r")
games = f.readlines()

result = 0
for game in games:
  game = re.sub("Game \d+\:","", game)
  plays = game.split(";")
  redCubes = []
  blueCubes = []
  greenCubes = []
  for play in plays:
    cubeSets = play.split(",")
    for cubeSet in cubeSets:
      cubes = cubeSet.split()
      count = int(cubes[0])
      color = cubes[1]
      if color == "red":
        redCubes.append(count)
      elif color == "blue":
        blueCubes.append(count)
      elif color == "green":
        greenCubes.append(count)
  result += max(redCubes) * max(blueCubes) * max(greenCubes)
print(result)

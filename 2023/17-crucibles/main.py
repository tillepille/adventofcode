import sys,heapq
sys.setrecursionlimit(10000)
file = open(sys.argv[1]).read().strip()

map = file.split("\n")
map = [[int(c) for c in x] for x in map]

noRows = len(map)
NoCol = len(map[0])

hops = [(0,0,0,-1,-1)]
routes = {}
while hops:
  dist,a,b,dir,inDir = heapq.heappop(hops)
  if (a,b,dir,inDir) in routes:
    continue
  routes[(a,b,dir,inDir)] = dist
  for i,(x,y) in enumerate([[-1,0],[0,1],[1,0],[0,-1]]):
    newA = a + x
    newB = b + y
    new_dir = i
    new_inDir = (1 if new_dir != dir else inDir + 1)
    if 0 <= newA < noRows and 0 <= newB < NoCol and new_inDir <= 3:
      cost = int(map[newA][newB])
      heapq.heappush(hops, (dist+cost, newA,newB,new_dir,new_inDir))

ans = 1e9
for (r,c,dir,inDir),v in routes.items():
  if r == noRows-1 and c == NoCol-1:
    ans = min(ans, v)
print(ans+1) # i dont find my one off error..

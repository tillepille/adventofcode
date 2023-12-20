import sys
file = open(sys.argv[1]).read().strip()
lines = file.split("\n\n")[0].split("\n")

lowImpulses = 0
highImpulses = 0
funcs = {}
pulseList = []
initializer = []

class PulseModule:
  def __init__(self, name, inputs, targets):
    self.name = name
    self.status = 0
    self.inputs = {name : 0 for name in inputs}
    self.targets = targets

  def __str__(self):
    return f"{self.name} {self.status} {self.inputs}"
    
  def forward(self, pulse):
    for i in self.targets:
      pulseList.append((i,self.name, pulse))

class Flipflop(PulseModule):
  def call(self,caller, pulse):
    if pulse == 0:
      if self.status == 0:
        self.status = 1
        self.forward(1)
      else:
        self.status = 0
        self.forward(0)

class Conjunction(PulseModule):
  def call(self, caller ,pulse):
    self.inputs[caller] = pulse
    if all(x == 1 for x in self.inputs.values()):
      self.forward(0)
    else:
      self.forward(1)

def findInputs(name):
  inputs = []
  for line in lines:
    caller, targets= line.split('->')
    if name in [x.strip() for x in targets.split(',')]:
      inputs.append(caller[1:].strip())
  return inputs

for line in lines:
  name, targets= line.split('->')
  targets = [x.strip() for x in targets.split(',')]
  if name.startswith('%'):
    name = name[1:].strip()
    inputs = []
    funcs[name] = Flipflop(name, inputs, targets)
  if name.startswith('&'):
    name = name[1:].strip()
    inputs = findInputs(name)
    funcs[name] = Conjunction(name, inputs, targets)
  if name.startswith('broadcaster'):
    for target in targets:
      pulseList.append((target, name, 0))
      initializer = pulseList.copy()


for i in range(1000):  
  lowImpulses += 1
  while pulseList:
    pulse = pulseList.pop(0)
    if pulse[2] == 0:
      lowImpulses += 1
    else:
      highImpulses += 1
    if pulse[0] in funcs.keys():
      funcs[pulse[0]].call(pulse[1], pulse[2])
  pulseList = initializer.copy()

print(lowImpulses, highImpulses)
print(lowImpulses * highImpulses)
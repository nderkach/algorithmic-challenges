import random
import operator

class Box(object):
    def __init__(self, w, h, d):
        self.w = w
        self.h = h
        self.d = d 

    def __str__(self):
        return "Box ({} {} {})".format(self.w, self.h, self.d)

boxes = [Box(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)) for _ in range(10)]
wsorted = sorted(boxes, key=operator.attrgetter('w'), reverse=True)
print([str(b) for b in wsorted])
hsorted = sorted(boxes, key=operator.attrgetter('h'), reverse=True)
print([str(b) for b in hsorted])
dsorted = sorted(boxes, key=operator.attrgetter('d'), reverse=True)
print([str(b) for b in dsorted])


count = 1
comp = wsorted[0]
stack = [comp]
for i in range(len(boxes)):
    if hsorted[i].w < comp.w and hsorted[i].h < comp.h and hsorted[i].d < comp.d:
        count += 1
        comp = hsorted[i]
        stack.append(hsorted[i])
        break

for i in range(len(boxes)):
    if dsorted[i].w < comp.w and dsorted[i].h < comp.h and dsorted[i].d < comp.d:
        stack.append(dsorted[i])
        count += 1
        break

print(count)
print([str(e) for e in stack])
print(sum([e.h for e in stack]))


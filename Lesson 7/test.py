import random

bkkk = str([(sorted(random.sample(range(1, 91), 4))) for i in range(5)])
print('  '.join(str(i) for i in bkkk))

print('__________________________')

bkkk2 = str([(sorted(random.sample(range(1, 91), 4))) for i in range(5)])

bkkk2 = line.split()
for i in range(3):
    bkkk2.insert("  ", bkkk2[i])
print(' '.join(bkkk2))

for i in bkkk2:
    print(('{:>3} ' * len(i)).format(*i))

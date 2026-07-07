#count é um iterador sem fim (itertools)
from itertools import count

c1 = count(10) # é um contador infinito
r1 = range(10, 100) # precisa de um limite pre-definido

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('c1', hasattr(r1, '__iter__'))
print('c1', hasattr(r1, '__next__'))
print()
print('---count---')
for i in c1:
    if i >= 100:
        break
    print(i)
print()
print('---range---')
for i in r1:
    print(i)

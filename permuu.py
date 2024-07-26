from itertools import permutations
c=permutations([1,4,3],3)
v=[int(i) for i in str(c)]
for i in v:
 print(i)
